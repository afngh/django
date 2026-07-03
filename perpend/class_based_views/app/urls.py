from django.urls import path
from .views import MyView

urlpatterns = [
    path('cv/', MyView.as_view(), name='my_view'),
]