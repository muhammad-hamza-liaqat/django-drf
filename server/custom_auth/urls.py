from django.urls import path
from .views import RegisterUser, LoginUser

urlpatterns = [
    path("sign_in/", RegisterUser.as_view(), name="sign-in"),
    path("login/", LoginUser.as_view(), name="login")
]