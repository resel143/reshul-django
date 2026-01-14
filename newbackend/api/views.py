from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from .db import book_collection

# Dummy data 
book_list = [
    {
        "id": 1,
        "title": "The Silent Forest",
        "author": "Arjun Mehta",
        "published_date": "2022-01-02",
        "genre": "Mystery",
        "isbn": "978-93-12345-01-2",
        "price": 399.00,
        "rating": 4.5,
        "pages": 320,
        "language": "English",
        "publisher": "BlueLeaf Publications",
        "available": True
    },
    {
        "id": 2,
        "title": "Code Beyond Logic",
        "author": "Reshul Wate",
        "published_date": "2023-03-15",
        "genre": "Technology",
        "isbn": "978-93-12345-02-9",
        "price": 599.00,
        "rating": 4.8,
        "pages": 410,
        "language": "English",
        "publisher": "TechVerse",
        "available": True
    },
    {
        "id": 3,
        "title": "Echoes of Time",
        "author": "Neha Sharma",
        "published_date": "2021-11-21",
        "genre": "Historical Fiction",
        "isbn": "978-93-12345-03-6",
        "price": 299.00,
        "rating": 4.1,
        "pages": 280,
        "language": "Hindi",
        "publisher": "Saffron Ink",
        "available": False
    },
    {
        "id": 4,
        "title": "AI for Humans",
        "author": "Dr. Vikram Rao",
        "published_date": "2024-06-10",
        "genre": "Artificial Intelligence",
        "isbn": "978-93-12345-04-3",
        "price": 749.00,
        "rating": 4.9,
        "pages": 520,
        "language": "English",
        "publisher": "FutureMind Press",
        "available": True
    },
    {
        "id": 5,
        "title": "Minimal Life",
        "author": "Aanya Kapoor",
        "published_date": "2020-09-05",
        "genre": "Self Help",
        "isbn": "978-93-12345-05-0",
        "price": 249.00,
        "rating": 3.9,
        "pages": 190,
        "language": "English",
        "publisher": "ZenHouse",
        "available": True
    },
    {
        "id": 6,
        "title": "The Last Algorithm",
        "author": "Kunal Deshmukh",
        "published_date": "2025-01-01",
        "genre": "Sci-Fi",
        "isbn": "978-93-12345-06-7",
        "price": 899.00,
        "rating": 4.7,
        "pages": 610,
        "language": "English",
        "publisher": "Nova Reads",
        "available": False
    }
]

@api_view(['GET'])
def get_book_list(request):
    books = list(book_collection.find({}))
    for book in books:
         book['_id'] = str(book['_id'])

    return Response({
        'status':200,
        'data': books
        })

@api_view(['GET'])
def get_book_by_title(request, book_name):
     
     
     matching_book = list(
          book_collection.find(
               {'title': {'$regex': book_name, '$options':'i'}}
          )
     )

     for book in matching_book:
          book['_id'] = str(book['_id'])

     if matching_book:
          return Response({
                    'message': f'{len(matching_book)} book(s) Found Successfully!',
                    'total': len(book_list),
                    'data': matching_book
               }, status=status.HTTP_200_OK)
          
     return Response({
          'error':'Book not found!',
     }, status=status.HTTP_400_BAD_REQUEST)  
          

@api_view(['POST'])
def add_book(request):
    data = request.data

    new_book = {
        "title": str(data.get("title", "")),
        "author": str(data.get("author", "")),
        "published_date": str(data.get("published_date", "")),
        "genre": str(data.get("genre", "")),
        "isbn": str(data.get("isbn", "")),
        "price": float(data.get("price", 0)),
        "rating": float(data.get("rating", 0)),
        "pages": int(data.get("pages", 0)),
        "language": str(data.get("language", "")),
        "publisher": str(data.get("publisher", "")),
        "available": bool(data.get("available", True))
    }

    result = book_collection.insert_one(new_book)

    new_book['_id'] = str(result.inserted_id)

    return Response(
        {
            "message": "Book added successfully",
            "data": new_book,
            "total_books": len(book_list)
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['PATCH'])
def update_book(request):
    data = request.data
    book_id = data.get('_id')

    if not book_id:
        return Response({'error': 'Book ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Only include allowed fields to update
    allowed_fields = {
        "title", "author", "published_date", "genre",
        "isbn", "price", "rating", "pages",
        "language", "publisher", "available"
    }

    update_fields = {field: data[field] for field in allowed_fields if field in data}

    if not update_fields:
        return Response({'message': 'No fields to update provided!'}, status=status.HTTP_400_BAD_REQUEST)

    # Update in MongoDB
    result = book_collection.update_one({'_id': ObjectId(book_id)}, {'$set': update_fields})

    if result.matched_count == 0:
        return Response({'error': 'No Book Found!'}, status=status.HTTP_404_NOT_FOUND)

    # Fetch the updated document
    book = book_collection.find_one({'_id': ObjectId(book_id)})

    book['_id'] = str(book['_id'])

    return Response({
        'message': 'Book Updated',
        'data': book,
    }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_book(request):
     data = request.data

     book_id = data.get('_id')

     if not book_id:
          return Response({
               'error': 'Book does not exists!!'
          }, status=status.HTTP_404_NOT_FOUND)
     
     result = book_collection.delete_one({'_id': ObjectId(book_id)})

     if result.deleted_count == 0:
        return Response({'error': 'Book not found!'}, status=status.HTTP_404_NOT_FOUND)
    
     return Response({
         'message': 'Book Deleted successfully',
     }, status=status.HTTP_200_OK)