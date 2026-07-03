from django.shortcuts import render
from django.views import View

class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id

class UserView(View):
    def get(self, request, username, id):
        user = User(username, id)
        return render(request, 'app/index.html', {'user': user})