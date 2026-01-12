from django.urls import path
from .views import hello_user

urlpatterns = [
    path('hello/', hello_user, name='Hi')
]