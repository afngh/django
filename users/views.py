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
            password = serializer.cleaned_data['password']

            hashed_password = make_password(password)

            user = serializer.save(password=hashed_password)

            return Response({
                "status":"success"
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "status":"failed"
        }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            "status":"failed"
        }, status=status.HTTP_401_UNAUTHORIZED)