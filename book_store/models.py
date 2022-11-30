from django.db import models

class Book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField(auto_now_add=True)

