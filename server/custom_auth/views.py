from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password, check_password
from custom_auth.models import User
from custom_auth.serializer import LoginSerializer
from custom_auth.helper import get_tokens_for_user


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        userName = data.get("userName")
        email = data.get("email")
        password = data.get("password")

        # Validate required fields
        if not all([userName, email, password]):
            return Response({
                "status": 400,
                "message": "userName, email, and password are required fields"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return Response({
                "status": 400,
                "message": "A user with this email already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if userName already exists
        if User.objects.filter(userName=userName).exists():
            return Response({
                "status": 400,
                "message": "A user with this userName already exists"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create user with hashed password
            hashed_password = make_password(password)
            user = User.objects.create(
                userName=userName,
                email=email,
                password=hashed_password
            )
            user.save()

            return Response({
                "status": 201,
                "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                "status": 500,
                "message": "An internal server error occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            user = serializer.validated_data['user']

            # Generate tokens for the user
            tokens = get_tokens_for_user(user)
            return Response({
                "status": 200,
                "message": "User logged in successfully",
                "tokens": tokens,
                "data": {
                    "email": user.email,
                    "userName": user.userName
                }
            }, status=status.HTTP_200_OK)
        else:
            # Return validation errors
            return Response({
                "status": 400,
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
