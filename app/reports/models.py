from django.db import models
from django.urls import reverse


class YearClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "YearClass"
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("year-class-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name.title()


class Student(models.Model):
    student_id = models.CharField(max_length=255, unique=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject, blank=True)
    year_class = models.ForeignKey( YearClass,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="student_year_classes",
    )

    class Meta:
        ordering = ("last_name", "first_name")

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.last_name}, {self.first_name} (ST) | ({self.student_id})"


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=255, unique=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return f" {self.last_name}, {self.first_name} (TR)"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name.title()


class Remark(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, related_name="student_remarks", on_delete=models.CASCADE
    )
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("remark-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} - {self.student.first_name} {self.student.last_name}"
