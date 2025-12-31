from django.core.management.base import BaseCommand
from api.models import Service, Portfolio, Testimonial, SiteSettings


class Command(BaseCommand):
    help = "Load initial data from the original website"

    def handle(self, *args, **options):
        # Create Site Settings
        settings, created = SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                "site_name": "GROWTHIFY",
                "hero_title": "WEB DEV & DIGITAL MARKETING",
                "hero_subtitle": "We help your business to grow online with minimal efforts and helps you to grow your business",
                "about_title": "We are the team of expert digital marketers and web developers",
                "about_description": "GROWTHIFY. is a leading Website Development and Digital marketing Company in indore with a team of professional developers and digital marketer dedicated to working with proficient coding skills and expertise that grab consumers' attention toward your business online.",
                "phone_1": "+91 8989282885",
                "phone_2": "+91 8815152801",
                "whatsapp_number": "+918989282885",
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Created site settings"))

        # Create Services
        services_data = [
            {
                "title": "Web Development",
                "description": "Design your first impression exaltedly! What if you get a beautifully designed website that attracts clients in the first blink? We are an excellent Web development company where our experts create enthralling websites for your business.",
                "icon": "code",
                "order": 1,
            },
            {
                "title": "Digital marketing",
                "description": "Boost your online presence with precision-targeted campaigns and innovative strategies. Our digital marketing services are designed to engage your audience and drive measurable results",
                "icon": "marketing",
                "order": 2,
            },
            {
                "title": "Video Editing",
                "description": "Transform raw footage into captivating stories with our expert video editing services. We create visually stunning and impactful videos that leave a lasting impression on your audience.",
                "icon": "video",
                "order": 3,
            },
        ]

        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data["title"], defaults=service_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created service: {service.title}")
                )

        # Create Portfolio
        portfolio_data = [
            {
                "title": "Anubhuti Donation Management Software",
                "description": "A desktop-based donation management system developed to efficiently record, track, and manage donations with secure data handling, donor records, and transparent reporting for organizations.",
                "category": "Web Development",
                "order": 1,
            },
            {
                "title":"Career & Job Opportunity Portal",
                "description": "FreshersHunt.in is an online career resource platform focused on helping students, fresh graduates ,and early-career professionals find IT jobs, off-campus drives, internships, and free learningresources across India",
                "category": "Web Development",
                "order": 2,
            },
            {
                "title": "Web Development",
                "description": "A user-friendly platform for renting bikes, offering a seamless booking process, location-based services, and detailed bike listings. The website is designed to make it easy for users to browse and rent bikes on the go.",
                "category": "Web Development",
                "order": 3,
            },
            {
                "title": "Course Selling website",
                "description": "An e-commerce platform built to sell online courses. It features a dynamic course catalog, secure payment integration, and a student dashboard, providing an efficient and engaging learning experience.",
                "category": "Web Development",
                "order": 4,
            },
            {
                "title": "Registrar Panel",
                "description": "A robust dashboard built for hosting providers to efficiently manage domain registrations, client accounts, and hosting plans. The interface provides real-time analytics, user management, and easy access to hosting services, streamlining the entire registrar process",
                "category": "Web Development",
                "order": 5,
            },
            {
                "title": "Food Deals",
                "description": "A visually appealing website design focused on providing users with the best food deals. The layout is optimized for easy navigation, allowing users to quickly find and claim offers at their favorite restaurants.",
                "category": "Web Development",
                "order": 6,
            },
        ]

        for portfolio_data_item in portfolio_data:
            portfolio, created = Portfolio.objects.get_or_create(
                title=portfolio_data_item["title"], defaults=portfolio_data_item
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created portfolio: {portfolio.title}")
                )

        # Create Testimonials
        testimonials_data = [
            {
                "client_name": "Er amit upadhyay",
                "content": "The product quality is consistently outstanding, exceeding my expectations every time",
                "rating": 5,
                "order": 1,
            },
            {
                "client_name": "Lucky Pal",
                "content": "They have very good web development team, they have made my coaching website",
                "rating": 5,
                "order": 2,
            },
            {
                "client_name": "The Mg",
                "content": "Growthifyservices boosted our revenue and brand awareness with their exceptional marketing strategies. Their tailored approach delivered impressive results.",
                "rating": 5,
                "order": 3,
            },
            {
                "client_name": "Om patel",
                "content": "I'm very satisfied with Growthifyservices' web development. The team was professional and delivered a fast, visually appealing website with excellent SEO. Highly recommend!",
                "rating": 5,
                "order": 4,
            },
        ]

        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                client_name=testimonial_data["client_name"], defaults=testimonial_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created testimonial: {testimonial.client_name}"
                    )
                )

        self.stdout.write(self.style.SUCCESS("Successfully loaded all initial data!"))
