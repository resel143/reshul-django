from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': "Reshul!!!"
    }
    return render(request, "index.html", context)


def about(request):
    return HttpResponse("This is About Page")