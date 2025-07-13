from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.utils.text import slugify
from drf_spectacular.utils import extend_schema, OpenApiExample

from .permissions import IsAdminOrReadOnly
from .models import Project, Service, AboutMe, Contact
from .serializers import ProjectSerializer, ServiceSerializer, AboutMeSerializer, ContactSerializer

def home(request):
    return HttpResponse("Welcome to My Portfolio Backend!")

# 📁 Projects
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        summary="List all projects",
        responses=ProjectSerializer,
        tags=["Projects"],
        examples=[
            OpenApiExample(
                name="List Projects Response",
                value={
                    "count": 1,
                    "next": None,
                    "previous": None,
                    "results": [
                        {
                            "id": 1,
                            "title": "My Portfolio App",
                            "description": "A mobile app built with Flutter",
                            "technology": "Flutter",
                            "web_link": "https://myportfolio.com",
                            "github_link": "https://github.com/user/repo"
                        }
                    ]
                },
                response_only=True
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new project",
        request=ProjectSerializer,
        responses=ProjectSerializer,
        tags=["Projects"],
        examples=[
            OpenApiExample(
                name="Create Project Example",
                value={
                    "title": "My Portfolio App",
                    "description": "A mobile app built with Flutter",
                    "technology": "Flutter",
                    "web_link": "https://myportfolio.com",
                    "github_link": "https://github.com/user/repo"
                },
                request_only=True
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        summary="Retrieve a single project",
        responses=ProjectSerializer,
        tags=["Projects"]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Update a project",
        request=ProjectSerializer,
        responses=ProjectSerializer,
        tags=["Projects"]
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        summary="Delete a project",
        tags=["Projects"]
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# 🛠 Services
class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        summary="List all services",
        responses=ServiceSerializer,
        tags=["Services"],
        examples=[
            OpenApiExample(
                name="List Services Response",
                value={
                    "count": 1,
                    "next": None,
                    "previous": None,
                    "results": [
                        {
                            "id": 1,
                            "title": "Web Development",
                            "description": "Building responsive websites with Django and React."
                        }
                    ]
                },
                response_only=True
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new service",
        request=ServiceSerializer,
        responses=ServiceSerializer,
        tags=["Services"],
        examples=[
            OpenApiExample(
                name="Create Service Example",
                value={
                    "title": "Web Development",
                    "description": "Building responsive websites with Django and React."
                },
                request_only=True
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ServiceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(summary="Retrieve a service", responses=ServiceSerializer, tags=["Services"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(summary="Update a service", request=ServiceSerializer, responses=ServiceSerializer, tags=["Services"])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(summary="Delete a service", tags=["Services"])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# 🧠 About Me
class AboutMeView(APIView):
    serializer_class = AboutMeSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        summary="View About Me",
        responses=AboutMeSerializer,
        tags=["About"],
        examples=[
            OpenApiExample(
                name="About Me Response Example",
                value={
                    "bio": "I'm a full-stack developer passionate about solving real-world problems with code.",
                    "location": "Lagos, Nigeria",
                    "email": "okonicha@example.com"
                },
                response_only=True
            )
        ]
    )
    def get(self, request):
        about = AboutMe.objects.first()
        if not about:
            return Response({"error": "About Me info not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutMeSerializer(about)
        return Response(serializer.data)

    @extend_schema(summary="Update About Me", request=AboutMeSerializer, responses=AboutMeSerializer, tags=["About"])
    def put(self, request):
        about = AboutMe.objects.first()
        if not about:
            return Response({"error": "About Me info not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutMeSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 📞 Contact
class ContactView(APIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAdminOrReadOnly]

    @extend_schema(
        summary="View Contact Info",
        responses=ContactSerializer,
        tags=["Contact"],
        examples=[
            OpenApiExample(
                name="Contact Response Example",
                value={
                    "phone": "+234123456789",
                    "email": "okonicha@example.com",
                    "location": "Lagos, Nigeria"
                },
                response_only=True
            )
        ]
    )
    def get(self, request):
        contact = Contact.objects.first()
        if not contact:
            return Response({'error': 'Contact info not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    @extend_schema(summary="Update Contact Info", request=ContactSerializer, responses=ContactSerializer, tags=["Contact"])
    def put(self, request):
        contact = Contact.objects.first()
        if not contact:
            return Response({'error': 'Contact info not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
