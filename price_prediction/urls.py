"""price_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core import views as core_views

schema_view = get_schema_view(
    openapi.Info(
        title="Car Price Prediction",
        default_version='v1',),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('', core_views.UserLoginView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('register/', core_views.UserRegisterView.as_view(), name="register"),
    path('login/', core_views.UserLoginView.as_view(), name='login'),
    path('logout/', core_views.LogoutView.as_view(), name='logout'),
    path('cars/', include('core.urls')),
    path('api/', include('api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]