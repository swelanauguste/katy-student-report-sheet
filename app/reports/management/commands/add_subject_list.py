from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Subject

SUBJECT_LIST = [
    "mathematics",
    "english a",
    "integrated science",
    "food and nutrition",
    "accounts",
    "health",
    "information technology",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in SUBJECT_LIST:
            name = _.lower()
            description = fake.sentence(nb_words=10, variable_nb_words=False)
            Subject.objects.get_or_create(name=name, description=description)
            self.stdout.write(self.style.SUCCESS(f"{name}"))
