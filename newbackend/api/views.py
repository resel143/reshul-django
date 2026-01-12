from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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
    return Response({
        'status':200,
        'data': book_list
        })

@api_view(['GET'])
def get_book_by_id(request, book_id):
     
     for book in book_list:
          if book['id'] == book_id:
               return Response({
                    'message':'Book found successfully',
                    'data': book,
                    'total':len(book_list)
               }, status=status.HTTP_200_OK)
    
     return Response({
          'error':'Book not found!',
          'total':len(book_list)
     }, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def get_book_by_title(request, book_name):
     
     matching_book = [
          book for book in book_list if book_name.lower() in book['title'].lower()
     ]

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

    # Generate new ID safely
    new_id = book_list[-1]["id"] + 1 if book_list else 1

    # Create new book dict (JSON-safe)
    new_book = {
        "id": int(new_id),
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

    # Append to global list
    book_list.append(new_book)

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

    book_id = data.get('id')

    if not book_id:
            return Response({
                'message': "Book ID is required!"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    for book in book_list:
         if int(book_id) == book['id']:
                book['title'] = str(data.get('title', book['title']))
                book['author'] = str(data.get('author', data['author']))
                book["published_date"] = data.get("published_date", book["published_date"])
                book["genre"] = data.get("genre", book["genre"])
                book["isbn"] = data.get("isbn", book["isbn"])
                book["price"] = float(data.get("price", book["price"]))
                book["rating"] = float(data.get("rating", book["rating"]))
                book["pages"] = int(data.get("pages", book["pages"]))
                book["language"] = data.get("language", book["language"])
                book["publisher"] = data.get("publisher", book["publisher"])
                book["available"] = bool(data.get("available", book["available"]))

                return Response({
                     'message': 'Book updated successfully',
                     'data': book,
                     'total': len(book_list)
                },
                    status=status.HTTP_200_OK
                )
    
    return Response({
         'error':'No Book Found!',
    }, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_book(request):
     data = request.data

     book_id = data.get('id')

     if not book_id:
          return Response({
               'error': 'Book does not exists!!'
          }, status=status.HTTP_404_NOT_FOUND)
     
     for index, book in enumerate(book_list):
          if int(book_id) == book['id']:
               deleted_book = book_list.pop(index)

               return Response({
                    'message': 'Book deleted successfully!',
                    'data': deleted_book,
                    'total':len(book_list)
               }, status=status.HTTP_200_OK)
          
    
     return Response({
         'error': 'Book not found!!',
            'total': len(book_list)
        }, status=status.HTTP_400_BAD_REQUEST)