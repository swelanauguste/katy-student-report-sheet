from django.core.management.base import BaseCommand
from faker import Faker

from ...models import YearClass


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for year in range(1, 6):
            for class_ in range(1, 5):
                YearClass.objects.get_or_create(
                    name=f"{year} - {class_}",
                    description=fake.sentence(nb_words=9, variable_nb_words=False)
                )
                self.stdout.write(self.style.SUCCESS(f"{year} - {class_}"))
