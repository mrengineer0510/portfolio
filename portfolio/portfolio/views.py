
from django.http import HttpResponse
from django.shortcuts import render


def homepg(request):
    return render(request, "index.html")
def menu(request):
    return render(request, "menu.html")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render (request, "projects.html")

def inf(request):
    return render(request, "info.md")
