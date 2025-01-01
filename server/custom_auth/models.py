from django.db import models

class User (models.Model):
    email = models.CharField(max_length=20)
    userName = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)