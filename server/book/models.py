from django.db import models

class Book (models.Model):
    title= models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=30, default='English')

    # def __str__(self):
    #     return self.title

