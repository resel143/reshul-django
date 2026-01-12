from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def hello_user(request):
    return Response({
        "message": "This is my first API",
        "status": 200
    })