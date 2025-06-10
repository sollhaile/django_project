#from django.http import HttpResponse
#def test_view(request):
#    return HttpResponse("TEST VIEW WORKS!")  # Simple response

from rest_framework import generics
from models import Book
from serializers import BookSerializer
class BookListCreateAPIVIEW(generics.ListCreateAPIView):
    """
    API view to retrieve list of books or create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer