from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',  # Change to your preferred username
                email='Aynekulu4341@gmail.com',  # Change to your preferred email
                password='Am@mt4188'  # Use a strong password
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
