from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    return Response(book_list)