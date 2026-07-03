from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request):
        return HttpResponse('Hello, this is a GET request!')

    def post(self, request):
        return HttpResponse('Hello, this is a POST request!')