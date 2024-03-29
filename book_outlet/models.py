from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"