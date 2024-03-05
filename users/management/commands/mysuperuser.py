# import os
# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         if not User.objects.filter(username='oreaba').exists():
#             User.objects.create_superuser('oreaba',
#                                           'm.h.oreaba@gmail.com',
#                                           '@E000000')

import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username="oreaba").exists():
            password = os.environ.get("SUPERUSER_PASSWORD")
            if password is None:
                raise ValueError("Password not found")
            User.objects.create_superuser(
                username="oreaba",
                email="email@xyz.com", 
                password='password',
            )
            print("Superuser has been created.")
        else:
            print("Superuser exists")