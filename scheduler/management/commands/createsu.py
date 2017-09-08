import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


MOTOS_MEXICO_ADMIN_USERNAME = os.getenv('MOTOS_MEXICO_ADMIN_USERNAME')
MOTOS_MEXICO_ADMIN_EMAIL = os.getenv('MOTOS_MEXICO_ADMIN_EMAIL')
MOTOS_MEXICO_ADMIN_PASSWORD = os.getenv('MOTOS_MEXICO_ADMIN_PASSWORD')


class Command(BaseCommand):

    def handle(self, *arg, **options):
        if not User.objects.filter(username=MOTOS_MEXICO_ADMIN_USERNAME).exists():
            User.objects.create_superuser(
                MOTOS_MEXICO_ADMIN_USERNAME,
                MOTOS_MEXICO_ADMIN_EMAIL,
                MOTOS_MEXICO_ADMIN_PASSWORD
            )
