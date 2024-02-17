from django.contrib.auth.models import User
from django.db.models import Avg

from rest_framework import serializers

from author.models import Author
from book.models import Book, Review

        
class BookSerializer(serializers.ModelSerializer):
    id = serializers.CharField(write_only=False, read_only=True)
    average_rating = serializers.CharField(write_only=False, read_only=True)
    
    class Meta:
        model = Book
        fields = ['id','title','author','total_rating','average_rating']
        
    def calculate_average_rating(self, instance):
        average_rating = Review.objects.filter(book=instance).aggregate(avg_rating=Avg('rating'))['avg_rating']
        return average_rating

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['average_rating'] = self.calculate_average_rating(instance)
        return data

class BookReviewSerializer(serializers.ModelSerializer):
    id = serializers.CharField(write_only=False, read_only=True)

    class Meta:
        model = Review
        fields = ['id','author','book','rating','comment']