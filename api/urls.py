from django.urls import path, include
from rest_framework import routers

from api import views

app_name = 'api'
urlpatterns = [
    path('users/', views.UserViewSet.as_view(), name='users'),
    path('cars/', views.CarApiView.as_view(), name='list_cars'),
    path('cars/<int:pk>/delete', views.DeleteCarApiView.as_view(), name='delete_car'),
]