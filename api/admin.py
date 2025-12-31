from django.contrib import admin
from .models import Service, Portfolio, Testimonial, Contact, SiteSettings, Job


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'rating', 'order', 'is_active', 'created_at']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['client_name', 'content']
    list_editable = ['order', 'is_active']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'location', 'job_type', 'experience_required', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['job_type', 'location', 'department', 'is_active', 'is_featured', 'created_at']
    search_fields = ['title', 'description', 'required_skills', 'department']
    list_editable = ['is_active', 'is_featured', 'order']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'department', 'location', 'location_details', 'job_type')
        }),
        ('Experience & Skills', {
            'fields': ('experience_required', 'required_skills', 'preferred_skills')
        }),
        ('Job Details', {
            'fields': ('description', 'responsibilities', 'qualifications')
        }),
        ('Compensation & Benefits', {
            'fields': ('salary_range', 'benefits'),
            'classes': ('collapse',)
        }),
        ('Application Settings', {
            'fields': ('application_deadline', 'application_email', 'external_application_url')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'is_featured', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related()
