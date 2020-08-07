from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to delete all sample users"""

    def handle(self, *args, **options):
        """Handle the command"""

    get_user_model().objects.filter(is_staff=False).delete()
    print('Deleted')
