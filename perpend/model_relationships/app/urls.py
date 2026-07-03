from django.urls import path
from .views import DataView, AddUser

urlpatterns = [
    path('get/<str:username>/', DataView.as_view(http_method_names=['get']), name='get_user'),
    path('add/<str:username>/', AddUser.as_view(http_method_names=['post']), name='add_user'),
    path('add/<str:username>/<str:project_name>/', DataView.as_view(http_method_names=['post']), name='add_project'),
]