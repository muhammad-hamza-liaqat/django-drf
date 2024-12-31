from rest_framework.views import APIView
from rest_framework.response import Response

class CreateBook (APIView):
    def get(self, request):
        return Response({
            "status": 201,
            "message": "book created successfully",
            "data": "_id: 123456"
        })

class GetBook (APIView):
    def get (self, request):
        return Response({
            "status": "200",
            "message": "book fetched successfully"
        })