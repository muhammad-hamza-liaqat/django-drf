from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from custom_auth.models import User
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password


class RegisterUser(APIView):
    def post (self, request):
      print("RAW",request.body)
      data = request.data
      print("json data", data)
      userName = data.get("userName")
      email = data.get("email")
      password = data.get("password")
      if not all ([userName, email, password]):
         return Response({
            "status": 400,
            "message": "userName, email, password are required fields"
         }, status= status.HTTP_400_BAD_REQUEST)
      try:
         hashed_password = make_password(password)
         user = User.objects.create(userName=userName, email=email, password=hashed_password)
         user.save()
         return Response({
            "status": 201,
            "message": "user sign in successfully"
         }, status=status.HTTP_201_CREATED)
      except Exception as e:
         return Response({
            "status": 500,
            "message": "internal server error",
            "error": f"{str(e)}"
         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginUser (APIView):
   def post (self, request):
      data = request.data
      email = data.get("email")
      password = data.get("password")

      if not all ([email, password]):
         return Response({
            "status": 400,
            "message": "email and password are required"
         }, status=status.HTTP_400_BAD_REQUEST)
      try:
         user = User.objects.filter(email = email).first()
         if not user:
            return Response({
               "status": 404,
               "message": "try sign-in? user not exist!"
            }, status=status.HTTP_404_NOT_FOUND)
         if check_password(password, user.password):
            return Response({
               "status": 200,
               "message": "user login successfully"
            }, status=status.HTTP_200_OK)
         else:
            return Response({
               "status": 401,
               "message": "invalid password"
            }, status=status.HTTP_401_UNAUTHORIZED)
      except Exception as e:
         return Response({
            "status": 200,
            "message": "user login successfully",
            "error": f"{str(e)}"
         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)