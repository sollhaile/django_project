from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # Alternatively, you can specify fields explicitly
        # fields = ['id', 'title', 'author', 'published_date', 'isbn']