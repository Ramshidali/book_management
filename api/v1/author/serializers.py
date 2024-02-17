from django.contrib.auth.models import User
from author.models import Author
from book.models import Book

from rest_framework import serializers

class AuthorGetSerializer(serializers.ModelSerializer):
    total_books = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = ['id','name','total_rating','total_books']
        
    def get_total_books(self, instance):
        total_no_books =  Book.objects.filter(author=instance).count()
        return total_no_books
        
class AuthorPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name','total_rating']
