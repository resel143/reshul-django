from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home page by Reshul")


def about(request):
    return HttpResponse("This is About Page")