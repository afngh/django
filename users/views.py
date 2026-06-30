from django.shortcuts import render
from .models import Users
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            try:
                user = Users.objects.get(
                    username=username,
                )
            except Exception as e:
                return Response({
                    "success":False,
                    "status":401,
                    "message": "inavlid username or password"
                }, status=status.HTTP_401_UNAUTHORIZED)
            return Response({
                "success" : True,
                "status" : 201,
                "username" : user.username,
                "message": "login successful"
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "success" : False,
            "status" : 403,
            "message":"invalid request body"
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({
            "success" : False,
            "status" : 405,
            "message" : f"invalid method required POST but got {request.method}"
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            try:
                user = Users.objects.get(
                    username=username
                )

                if check_password(password, user.password):
                    return Response({
                        "success" : True,
                        "status" : 201,
                        "username" : user.username,
                        "message" : "login successful"
                    },status=status.HTTP_201_CREATED)
                else:
                    return Response({
                        "success" : False,
                        "status" : 401,
                        "message" : "inavalid password"
                    },status=status.HTTP_401_UNAUTHORIZED)
            except Exception as _:
                return Response({
                        "success" : False,
                        "status" : 401,
                        "message" : "inavalid username or password"
                    },status=status.HTTP_401_UNAUTHORIZED)
        return Response({
            "success" : False,
            "status" : 403
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({
            "success" : False,
            "status" : 400
        }, status=status.HTTP_400_BAD_REQUEST)