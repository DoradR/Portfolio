# Generated by Django 4.1.3 on 2022-11-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("DominikRadziszewski", "0003_post_picturesofpost"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="descriptionOfContat",
            new_name="descriptionOfContact",
        ),
    ]
