from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=255)
    catergory=models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    pages=models.IntegerField()
    price= models.IntegerField()
    stock=models.IntegerField()
    description=models.TextField()
    imageUrl=models.URLField()
    status=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True)
