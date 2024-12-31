from django.urls import path
from .views import GetBook, CreateBook

urlpatterns = [
    path("my-books/", GetBook.as_view(), name="get-book"),
    path("add-book/", CreateBook.as_view(), name="create-book"),
]