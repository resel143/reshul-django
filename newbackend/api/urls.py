from django.urls import path
from .views import get_book_list, add_book, update_book, delete_book, get_book_by_title

urlpatterns = [
    path('books/add', add_book, name='addBook'),
    path('books/delete', delete_book, name='deleteBook'),
    path('books/update', update_book, name='updateBook'),
    path('books/', get_book_list, name='getBook'),
    path('books/<str:book_name>', get_book_by_title, name='getBookByTitle'),
]