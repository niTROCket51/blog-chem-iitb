"""For populating database with csv file."""

import csv
from django.core.management.base import BaseCommand
from feed.models import Course

class Command(BaseCommand):
    """Populates model database with a .csv file."""
    help = 'Populates model database with a .csv file'

    def import_csv(self):
        """Function for extracting data and creating objects."""
        with open('feed/chemcourses.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                code = row[0]
                name = row[1]
                semester = row[2]

                try:
                    obj, created = Course.objects.get_or_create(
                        code=code,
                        name=name,
                        semester=eval(semester),
                    )
                    if created:
                        obj.save()

                except Exception as ex:
                    print(str(ex))

    def handle(self, *args, **options):
        self.import_csv()
