from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Portfolio, Testimonial, Contact, SiteSettings, Job
from .serializers import (
    ServiceSerializer, PortfolioSerializer, TestimonialSerializer,
    ContactSerializer, SiteSettingsSerializer, JobSerializer
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Portfolio.objects.filter(is_active=True)
    serializer_class = PortfolioSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=False, methods=['get'])
    def by_category(self, request):
        category = request.query_params.get('category', None)
        if category:
            portfolios = self.queryset.filter(category=category)
            serializer = self.get_serializer(portfolios, many=True)
            return Response(serializer.data)
        return Response([])


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post', 'get']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Send email notification to support@growthifyservices.in
        try:
            contact_data = serializer.validated_data
            subject = f"New Contact Form Submission from {contact_data['name']}"
            message = f"""
New contact form submission received:

Name: {contact_data['name']}
Email: {contact_data['email']}
Phone: {contact_data['phone']}

Message:
{contact_data['message']}

---
This is an automated notification from Growthify Contact Form.
            """
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
        except Exception as e:
            # Log the error but don't fail the request
            print(f"Error sending email notification: {e}")
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Thank you for contacting us! We will get back to you soon.'},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    
    def list(self, request, *args, **kwargs):
        instance = SiteSettings.objects.first()
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Job listings.
    Only returns active jobs, ordered by featured status and creation date.
    """
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get only featured jobs"""
        featured_jobs = self.queryset.filter(is_featured=True)
        serializer = self.get_serializer(featured_jobs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_department(self, request):
        """Filter jobs by department"""
        department = request.query_params.get('department', None)
        if department:
            jobs = self.queryset.filter(department__icontains=department)
            serializer = self.get_serializer(jobs, many=True)
            return Response(serializer.data)
        return Response([])
