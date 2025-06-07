from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "Bievenidos a mi primer programa en Django"}
    return render(request, "myapp/index.html", context)