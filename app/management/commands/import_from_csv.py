import csv
import random

from django.core.management.base import BaseCommand, CommandError

from app.models import Employee, Qualification

QUALIFICATIONS = [
    'Web programming',
    'Data bases',
    'Testing',
    'Designers',
    'Android',
    'Ios',
    'System programming',
    'Data protection'
]


class Command(BaseCommand):
    help = 'Import data from csv to db'

    qualifications = [Qualification(profile=q) for q in QUALIFICATIONS]

    def _create_employee(self, csv_file):
        with open(csv_file, newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                employee = Employee(
                    gender=row['gender'],
                    enrolled_university=row['enrolled_university'],
                    education_level=row['education_level'],
                    major_discipline=row['major_discipline'],
                    experience=row['experience'],
                    company_type=row['company_type'],
                    last_new_job=row['last_new_job'],
                    training_hours=row['training_hours'],
                    target=row['target'],
                    qualification=random.choice(self.qualifications)
                )
                print('.', sep='')

                yield employee

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        for qualification in self.qualifications:
            qualification.save()

        Employee.objects.bulk_create(
            objs=self._create_employee(csv_file),
            batch_size=500
        )

        self.stdout.write(self.style.SUCCESS('Success'))
