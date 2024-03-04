import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='oreaba').exists():
            User.objects.create_superuser('oreaba',
                                          'm.h.oreaba@gmail.com',
                                          '@E000000')
