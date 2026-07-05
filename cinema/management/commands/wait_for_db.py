import time
from django.core.management.base import BaseCommand
import django.db


class Command(BaseCommand):
    def handle(self, *args, **options):
        max_retries = 30
        retry_count = 0

        while retry_count < max_retries:
            try:
                django.db.connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available!"))
                return
            except Exception:
                retry_count += 1
                self.stdout.write(f"Waiting for database... ({retry_count}/{max_retries})")
                time.sleep(1)
        self.stdout.write(self.style.ERROR("Database is not available after max retries"))
        raise Exception("Database connection failed")
