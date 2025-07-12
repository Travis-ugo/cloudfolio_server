from django.urls import path
from . import views

urlpatterns = [
    # Home endpoint (optional)
    path('', views.home),

    # Project endpoints
    path('projects/', views.ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),

    # Service endpoints
    path('services/', views.ServiceListCreate.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),

    # About Me endpoint (typically just one record)
    path('about/<int:pk>/', views.AboutMeRetrieveUpdate.as_view(), name='about'),

    # Contact endpoint (POST-only)
    path('contact/', views.ContactCreate.as_view(), name='contact'),
]
