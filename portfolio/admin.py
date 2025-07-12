from django.contrib import admin
from .models import Project 

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'technology')
    ordering = ('-created_at',)
