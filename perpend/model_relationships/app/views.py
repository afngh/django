from django.shortcuts import render
from django.views import View
from .models import Projects, User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class DataView(View):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            projects = Projects.objects.filter(user=user)
            return render(request, 'app/data.html', {'user': user, 'projects': projects})
        except:
            return HttpResponse('User not found', status=404)
    def post(self, request, username, project_name):
        try:
            user = User.objects.get(username=username)
            project = Projects.objects.create(user=user, name=project_name)
            return HttpResponse(f'Project {project.name} created for user {user.username}', status=201)
        except:
            return HttpResponse('Error creating project', status=400)

@method_decorator(csrf_exempt, name='dispatch')
class AddUser(View):
    def post(self, request, username):
        try:
            user = User.objects.create(username=username)
            return HttpResponse(f'User {user.username} created', status=201)
        except:
            return HttpResponse('Error creating user', status=400)