# Generated by Django 4.2.5 on 2023-09-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="phone",
            field=models.CharField(default="", max_length=20),
        ),
    ]
