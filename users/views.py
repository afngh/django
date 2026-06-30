from django.shortcuts import render
from .models import Users
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']

            hashed_password = make_password(password)

            user = serializer.save(password=hashed_password)

            return Response({
                "success" : True,
                "status" : 201,
                "username" : user.username
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "success" : False,
            "status" : 403
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({
            "success" : False,
            "status" : 400
        }, status=status.HTTP_400_BAD_REQUEST)