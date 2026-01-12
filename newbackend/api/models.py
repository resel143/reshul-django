from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    published_date = models.DateField()
    genre=models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    price=models.DecimalField(max_digits=50, decimal_places=2)
    rating= models.FloatField()
    pages=models.IntegerField()
    language = models.CharField(max_length=40)
    publisher = models.CharField(max_length=80)
    available= models.BooleanField(default=True)

    def __str__(self):
        return self.title