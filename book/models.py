from django.db import models
from author.models import Author

from main.models import BaseModel

# Create your models here.
class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Review(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.name if self.author else ''} - {self.book.title if self.book else ''}"