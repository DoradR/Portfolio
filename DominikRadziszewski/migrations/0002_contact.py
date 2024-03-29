# Generated by Django 4.1.3 on 2022-11-08 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DominikRadziszewski", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("emailOfContact", models.CharField(max_length=64)),
                ("phoneOfContact", models.IntegerField()),
                ("descriptionOfContat", models.TextField(max_length=512)),
            ],
        ),
    ]
