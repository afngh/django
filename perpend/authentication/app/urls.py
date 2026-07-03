from django.urls import path
from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('logout/', LogoutView, name='logout'),
]