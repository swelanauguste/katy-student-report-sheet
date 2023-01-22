from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Student


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):
            student_id = fake.ean(length=8)
            first_name = fake.first_name()
            last_name = fake.last_name()
            Student.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                student_id=student_id,
            )
            self.stdout.write(self.style.SUCCESS(f"{student_id}"))
