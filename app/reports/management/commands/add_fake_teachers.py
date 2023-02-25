from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Teacher


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(40):
            teacher_id = fake.ean(length=8)
            first_name = fake.first_name()
            last_name = fake.last_name()
            # subject = Student.objects.get(
            #     pk=randint(Student.objects.first(), Student.objects.count())
            # )
            Teacher.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                teacher_id=teacher_id,
                # subject=subject,
            )
            self.stdout.write(self.style.SUCCESS(f"{teacher_id}"))
