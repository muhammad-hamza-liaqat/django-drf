from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, userName, password=None):
        if not email:
            raise ValueError("The Email field is required")
        if not userName:
            raise ValueError("The Username field is required")

        user = self.model(email=self.normalize_email(email), userName=userName)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, userName, password=None):
        user = self.create_user(email, userName, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    userName = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['userName']

    def __str__(self):
        return self.email
