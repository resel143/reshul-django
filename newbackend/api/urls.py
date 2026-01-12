from django.urls import path
from .views import get_book_list, add_book

urlpatterns = [
    path('books/', get_book_list, name='getBook'),
    path('books/add', add_book, name='addBook'),
]