# Generated by Django 4.1.1 on 2022-09-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UAM", "0006_alter_applications_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applications",
            name="name",
            field=models.CharField(
                choices=[
                    ("", ""),
                    ("Bellina", "Bellina"),
                    ("Sophos", "Sophos"),
                    ("Palladium", "Palladium"),
                ],
                default="",
                max_length=200,
                null=True,
            ),
        ),
    ]
