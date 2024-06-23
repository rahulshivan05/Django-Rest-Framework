from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
# from .views import api_home
urlpatterns = [
    path('', views.api_home),
    path('auth/', obtain_auth_token),
    path('create/', views.create_product),
]
