import time
from django.core.management.base import BaseCommand
import django.db


class Command(BaseCommand):
    def handle(self, *args, **options):

        while True:
            try:
                django.db.connection.ensure_connection()
                break
            except Exception:
                time.sleep(1)
