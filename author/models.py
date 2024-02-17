from django.db import models
from main.models import BaseModel

# Create your models here.
class Author(BaseModel):
    name = models.CharField(max_length=100)
    total_rating = models.FloatField(default=0)

    def __str__(self):
        return self.name