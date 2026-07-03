from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import ProfileForm

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_profile(request):
    
    if request.method == 'GET':
        form = ProfileForm()
        return render(request, 'app/upload.html', {'form': form})

    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_profile(request, username):
    try:
        profile = Profile.objects.get(username=username)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=404)

    return render(request, 'app/index.html', {'profile': profile})