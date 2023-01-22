from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Remark, Teacher, Student, Category

cat_count = Category.objects.count()
teacher_count = Teacher.objects.count()
student_count = Student.objects.count()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):
            category = Category.objects.get(pk=randint(1, cat_count))
            student = Student.objects.get(pk=randint(1, student_count))
            title = fake.sentence(nb_words=5, variable_nb_words=False)
            text = fake.sentence(nb_words=18, variable_nb_words=False)
            created_by = Teacher.objects.get(pk=randint(1, teacher_count))
            Remark.objects.get_or_create(
                category=category,
                student=student,
                title=title,
                text=text,
                created_by=created_by
            )
            self.stdout.write(self.style.SUCCESS(f"{title}"))
