from django.urls import path
from . import views
from .views import *


urlpatterns = [ 
    path('api/register/', RegisterAPIView.as_view()),
]