from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
=======
print("hello")
print("test")
>>>>>>> c5ab3fc12da9dd21ef540a5fbd36e7de499b0785
def home(request):
    return render(request, "index.html")
