# Generated by Django 4.1.5 on 2023-01-22 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0002_alter_student_options_alter_remark_student"),
    ]

    operations = [
        migrations.CreateModel(
            name="YearClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="remark",
            name="year_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reports.yearclass",
            ),
        ),
    ]
