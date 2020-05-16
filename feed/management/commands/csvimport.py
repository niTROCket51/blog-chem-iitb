"""For populating database with csv file."""

import csv
from django.core.management.base import BaseCommand
from .models import Course

class Command(BaseCommand):
    """Populates model database with a .csv file."""
    help = 'Populates model database with a .csv file'

    def handle(self, *args, **options):
        with open('feed/chemcourses.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                _, created = Course.objects.get_or_create(
                    code=row[0],
                    name=row[1],
                    semester=row[2],
                )

                self.stdout.write(self.style.SUCCESS('Added course "%s"' % row[0]))
