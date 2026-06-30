from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer, DefaultSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

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
                "username" : user.username,
                "message" : "registered successfully"
            },status=status.HTTP_201_CREATED)
        
        return Response({
            "success" : False,
            "status" : 403,
            "message" : "invalid data"
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({
            "success" : False,
            "status" : 400,
            "message" : f"invalid request expected POST but got {request.method}"
        }, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = DefaultSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            try:
                user = User.objects.get(
                    username=username
                )

                if check_password(password, user.password):

                    refresh = RefreshToken.for_user(user)

                    return Response({
                        "success" : True,
                        "status" : 200,
                        "username" : user.username,
                        "message" : "login successful",
                        "tokens":{
                            "refresh": str(refresh),
                            "access": str(refresh.access_token)
                        }
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
            "status" : 403,
            "message": "invalid data",
        }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({
            "success" : False,
            "status" : 400,
            "message" : f"invalid request expected POST but got {request.method}"

        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getall(request):
    users = User.objects.values('id','username')
    
    return Response({
        "success": True,
        "data": list(users)}
    )