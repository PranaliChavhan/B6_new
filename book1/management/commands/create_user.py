from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "Creates random users"

    def add_arguments(self, parser):
        parser.add_argument('total', type = int, help = 'Indicates no of users to be created')

    def handle(self,*args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(6), email='', password = '123') 