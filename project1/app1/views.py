from django.shortcuts import render
from django.http import HttpResponse
print("hello")
print("test")
def home(request):
    return render(request, "index.html")
