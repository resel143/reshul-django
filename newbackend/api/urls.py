from django.urls import path
from .views import get_book_list, add_book, update_book, delete_book, get_book_by_id

urlpatterns = [
    path('books/', get_book_list, name='getBook'),
    path('books/<int:book_id>', get_book_by_id, name='getBookById'),
    path('books/add', add_book, name='addBook'),
    path('books/update', update_book, name='updateBook'),
    path('books/delete', delete_book, name='deleteBook'),
]