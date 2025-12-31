from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, PortfolioViewSet, TestimonialViewSet, ContactViewSet, SiteSettingsViewSet, JobViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'portfolio', PortfolioViewSet, basename='portfolio')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
router.register(r'contact', ContactViewSet, basename='contact')
router.register(r'settings', SiteSettingsViewSet, basename='settings')
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('', include(router.urls)),
]

