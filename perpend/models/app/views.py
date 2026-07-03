from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import PerpendUsers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, username):
        try:
            user = PerpendUsers.objects.get(username=username)
            return render(request, 'app/index.html', {'user': user})
        except PerpendUsers.DoesNotExist:
            return HttpResponse('User not found', status=404)
    def post(self, request, username, number):
        try:
            user = PerpendUsers.objects.create(username=username, number=number)
            return HttpResponse(f'User {user.username} created with number {user.number}', status=201)
        except:
            return HttpResponse('Error creating user', status=400)