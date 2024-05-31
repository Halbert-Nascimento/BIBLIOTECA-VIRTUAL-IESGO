from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  published_date = models.DateField()
  book_cover = models.ImageField(upload_to='book_covers/', blank=True, null=True, default="book_covers/vazio.jpg")
  

  # def __str__(self):
  #   return self.title, self.author
