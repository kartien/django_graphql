from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    