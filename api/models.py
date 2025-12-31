from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)
    category = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    client_designation = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "created_at"]

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="GROWTHIFY")
    hero_title = models.CharField(max_length=200)
    hero_subtitle = models.TextField()
    about_title = models.CharField(max_length=200)
    about_description = models.TextField()
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]
    
    LOCATION_TYPE_CHOICES = [
        ('remote', 'Remote'),
        ('on-site', 'On-site'),
        ('hybrid', 'Hybrid'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200, help_text="Job title (e.g., Full Stack Developer)")
    department = models.CharField(max_length=100, help_text="Department (e.g., Engineering, Marketing)")
    location = models.CharField(max_length=100, choices=LOCATION_TYPE_CHOICES, default='remote')
    location_details = models.CharField(max_length=200, blank=True, null=True, help_text="Specific location if applicable")
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default='full-time')
    
    # Experience & Skills
    experience_required = models.CharField(max_length=50, help_text="e.g., 2-4 years, Entry Level, Senior")
    required_skills = models.TextField(help_text="Comma-separated skills (e.g., React, Node.js, Python)")
    preferred_skills = models.TextField(blank=True, null=True, help_text="Optional/preferred skills")
    
    # Job Details
    description = models.TextField(help_text="Brief job description")
    responsibilities = models.TextField(help_text="Key responsibilities (use line breaks for bullet points)", null=True, blank=True)
    qualifications = models.TextField(help_text="Required qualifications and requirements", null=True, blank=True)
    
    # Compensation & Benefits
    salary_range = models.CharField(max_length=100, blank=True, null=True, help_text="e.g., $50k-$70k, Competitive")
    benefits = models.TextField(blank=True, null=True, help_text="Benefits offered")
    
    # Application Details
    application_deadline = models.DateField(blank=True, null=True)
    application_email = models.EmailField(default="hr@growthifyservices.in")
    external_application_url = models.URLField(blank=True, null=True, help_text="External job posting URL if any")
    # Admin Controls
    is_active = models.BooleanField(default=True, help_text="Show this job on the website")
    is_featured = models.BooleanField(default=False, help_text="Feature this job at the top")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
        verbose_name = "Job Opening"
        verbose_name_plural = "Job Openings"
    
    def __str__(self):
        return f"{self.title} - {self.department}"
    
    def get_skills_list(self):
        """Return required skills as a list"""
        return [skill.strip() for skill in self.required_skills.split(',') if skill.strip()]
    
    def is_deadline_passed(self):
        """Check if application deadline has passed"""
        if self.application_deadline:
            from django.utils import timezone
            return timezone.now().date() > self.application_deadline
        return False
