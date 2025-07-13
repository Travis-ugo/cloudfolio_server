from rest_framework import serializers
from .models import Project, Service, AboutMe, Contact
from django.utils.text import slugify

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        if not validated_data.get('slug') and validated_data.get('title'):
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)    

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data.get('slug') and validated_data.get('title'):
            validated_data['slug'] = slugify(validated_data['title'])
        return super().create(validated_data)

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
