from .views import upload_profile, view_profile
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('upload/', upload_profile, name='upload_profile'),
    path('view/<str:username>/', view_profile, name='view_profile')
]
