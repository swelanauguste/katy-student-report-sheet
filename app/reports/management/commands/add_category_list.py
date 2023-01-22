from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category

CATEGORY_LIST = ["good", "bad", "ugly"]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in CATEGORY_LIST:
            name = _.lower()
            description = fake.sentence(nb_words=10, variable_nb_words=False)
            Category.objects.get_or_create(name=name, description=description)
            self.stdout.write(self.style.SUCCESS(f"{name}"))
