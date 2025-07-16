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
from django.urls import path, include
from portfolio.views import home
from rest_framework.authtoken import views as drf_auth_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views.auth import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # 🏠 Home
    path('', home, name='home'),

    # 🔐 Admin and Auth
    path('admin/', admin.site.urls),

    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📦 Portfolio app
    path('api/v1/', include(('portfolio.urls', 'portfolio'), namespace='portfolio')),

    # 📄 OpenAPI schema
    path('openapi/', SpectacularAPIView.as_view(), name='schema'),

    # 💠 Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # 📘 Redoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# 🧾 Serve static files during development (needed for Swagger UI)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
