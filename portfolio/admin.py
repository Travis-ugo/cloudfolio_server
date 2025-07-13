from django.contrib import admin
from .models import Project , AboutMe, Service, Contact
from django.http import HttpResponseRedirect
from django.urls import reverse

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'technology')
    ordering = ('-created_at',)

@admin.register(Service)    
class SeviceAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "icon")
    search_fields = ("title", "description")
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return AboutMe.objects.count() == 0
    
    def changelist_view(self, request, extra_context = None):
        queryset = AboutMe.objects.all()
        if queryset.exists():
            obj = queryset.first()
            return HttpResponseRedirect(
                reverse('admin:portfolio_aboutme_change', args = [obj.pk])
            )
        return super().changelist_view(request, extra_context)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return Contact.objects.count() == 0
    
    def changelist_view(self, request, extra_context = None):
        queryset = Contact.objects.all()
        if queryset.exists():
            obj = queryset.first()
            return HttpResponseRedirect(
                reverse('admin:portfolio_contact_change', args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)