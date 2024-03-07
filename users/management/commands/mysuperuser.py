# from django.contrib.auth.models import User
from users.models import PMUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not PMUser.objects.filter(username='admin').exists():
            PMUser.objects.create_superuser('admin',
                                          'admin@admin.com',
                                          '@E000000')
            print("Superuser has been created.")
        else:
            print("Superuser exists")