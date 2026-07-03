from django.urls import path
from .views import UserView

urlpatterns = [
    path('<str:username>/<int:id>/', UserView.as_view(), name='user_view'),
]