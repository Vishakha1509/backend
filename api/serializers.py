from rest_framework import serializers
from .models import Service, Portfolio, Testimonial, Contact, SiteSettings, Job


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'icon', 'order', 'created_at']


class PortfolioSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'description', 'image_url', 'category', 'link', 'order', 'created_at']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class TestimonialSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ['id', 'client_name', 'client_designation', 'content', 'image_url', 'rating', 'order', 'created_at']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'message', 'created_at']
        read_only_fields = ['created_at']


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ['site_name', 'hero_title', 'hero_subtitle', 'about_title', 'about_description',
                  'phone_1', 'phone_2', 'email', 'whatsapp_number', 'address']


class JobSerializer(serializers.ModelSerializer):
    required_skills_list = serializers.SerializerMethodField()
    preferred_skills_list = serializers.SerializerMethodField()
    is_deadline_passed = serializers.SerializerMethodField()
    location_display = serializers.CharField(source='get_location_display', read_only=True)
    job_type_display = serializers.CharField(source='get_job_type_display', read_only=True)
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'department', 'location', 'location_display', 
            'location_details', 'job_type', 'job_type_display', 
            'experience_required', 'required_skills', 'required_skills_list',
            'preferred_skills', 'preferred_skills_list', 'description', 
            'responsibilities', 'qualifications', 'salary_range', 'benefits',
            'application_deadline', 'application_email', 'external_application_url',
            'is_featured', 'is_deadline_passed', 'created_at', 'updated_at'
        ]
    
    def get_required_skills_list(self, obj):
        """Convert comma-separated skills to list"""
        return obj.get_skills_list()
    
    def get_preferred_skills_list(self, obj):
        """Convert comma-separated preferred skills to list"""
        if obj.preferred_skills:
            return [skill.strip() for skill in obj.preferred_skills.split(',') if skill.strip()]
        return []
    
    def get_is_deadline_passed(self, obj):
        """Check if application deadline has passed"""
        return obj.is_deadline_passed()
