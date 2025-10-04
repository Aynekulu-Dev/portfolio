from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='Aynekulu4341@gmail.com',
                password='NewAdminPass123!'  # Your new password here
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            # Reset existing superuser password
            superuser = User.objects.filter(is_superuser=True).first()
            superuser.set_password('NewAdminPass123!')  # Your new password here
            superuser.save()
            self.stdout.write(self.style.SUCCESS('Superuser password reset successfully'))