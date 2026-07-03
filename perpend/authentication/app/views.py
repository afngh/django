from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer

@api_view(['POST'])
def LoginView(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def LogoutView(request):
    logout(request)
    return Response({'message': 'Logout successful'})

@api_view(['POST'])
def RegisterView(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=request.data.get('password')
        )
        return Response({'message': 'User registered successfully'})
    else:
        return Response(serializer.errors, status=400)