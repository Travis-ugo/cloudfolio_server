"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from portfolio.views import home 
from django.urls import path, include
from rest_framework.authtoken import views as drf_auth_views
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularSwaggerView, 
    SpectacularRedocView
)

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', drf_auth_views.obtain_auth_token),
    path('api/v1/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),

    # 🌐 OpenAPI raw schema (for Postman or tooling)
    path('openapi/', SpectacularAPIView.as_view(), name='schema'),

    # 💠 Swagger UI (interactive API docs)
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # 📘 Redoc UI (cleaner docs)
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
