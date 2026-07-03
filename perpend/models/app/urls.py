from django.urls import path
from .views import UserView

urlpatterns = [
    path('<str:username>/', UserView.as_view(http_method_names=['get']), name='user_get_view'),
    path('<str:username>/<int:number>/', UserView.as_view(http_method_names=['post']), name='user_post_view'),
]