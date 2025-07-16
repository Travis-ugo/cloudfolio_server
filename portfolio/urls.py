from django.urls import path
from portfolio.views import (
    home,
    ProjectListCreate, ProjectRetrieveUpdateDestroy,
    ServiceListCreate, ServiceRetrieveUpdateDestroy,
    AboutMeView, ContactView
)

app_name = 'portfolio'

urlpatterns = [ 
    # 🏠 Home endpoint
    path('', home, name='home'),

    # 📁 Project endpoints
    path('projects/', ProjectListCreate.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
    # path('projects/action/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail-body'),

    # 🛠 Service endpoints
    path('services/', ServiceListCreate.as_view(), name='service-list'),
    path('services/<int:pk>/', ServiceRetrieveUpdateDestroy.as_view(), name='service-detail'),
    #  path('services/action/', ServiceRetrieveUpdateDestroy.as_view(), name='service-detail-body'),

    # 🧠 About Me endpoint
    path('about/', AboutMeView.as_view(), name='about'),

    # 📞 Contact endpoint
    path('contact/', ContactView.as_view(), name='contact'),
]
