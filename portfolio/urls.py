from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Home endpoint (optional)
    path('', views.home),

    # Project endpoints
    path('projects/', views.ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),

    # Service endpoints
    path('services/', views.ServiceListCreate.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),

    # About Me endpoint
    path('about/', views.AboutMeView.as_view(), name='about'),

    # Contact endpoint
    path('contact/', views.ContactView.as_view(), name='contact'),
]
