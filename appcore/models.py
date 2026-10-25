from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/")
    price = models.PositiveIntegerField(default=0)
    measurement = models.CharField(max_length=10, default=" ")
    
    def __str__(self):
        return self.name