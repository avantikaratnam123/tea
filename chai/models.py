from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=300)
    message=models.TextField(max_length=500)

class Product(models.Model):
    description=models.TextField()
    upload_image=models.ImageField(upload_to="product")

