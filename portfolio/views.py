from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Project, Service, AboutMe, Contact
from .serializers import ProjectSerializer, ServiceSerializer, AboutMeSerializer, ContactSerializer

def home(request):
    return HttpResponse("Welcome to My Portfolio Backend!")

# Projects
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Services
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# About Me (usually just one instance)
class AboutMeRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer

# Contact (POST only, no list view needed)
class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
