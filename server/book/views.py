from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from rest_framework.permissions import IsAuthenticated
# import json

class CreateBook(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # log raw request.body
        print("RAW",request.body)
        # logs the json data coverted into python object
        data = request.data
        print("Requested data",request.data)
        title = data.get("title")
        author = data.get("author")
        language = data.get("language", "English") 

        if not title or not author:
            return Response({
                "status": 400,
                "message": "Title or author is missing"
            }, status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.create(title=title, author=author, language=language)
        print("Book created:", book)
        return Response({
            "status": 201,
            "message": "Book created successfully",
            "data": {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "language": book.language
            },
        }, status=status.HTTP_201_CREATED)       

class GetBook (APIView):
    permission_classes = [IsAuthenticated]
    def get (self, request):
        books = Book.objects.all()
        print(books)
        book_list = [
            {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "language": book.language,
            }
            for book in books
        ]
        print(book_list)
        return Response({"status": 200, "message": "All books fetched successfully", "data": book_list}, status=status.HTTP_200_OK)