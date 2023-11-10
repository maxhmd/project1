from unicodedata import name
from django.db import models

class products(models.Model):
    name = models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=None, decimal_places=5)

"""
chaque fois je modifie ma table ou ma classe du model je besion de taper :
python manage.py makemigrations
python manage .py migrate 
"""

