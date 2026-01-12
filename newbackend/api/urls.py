from django.urls import path
from .views import get_book_list

urlpatterns = [
    path('hello/', get_book_list, name='Hi')
]