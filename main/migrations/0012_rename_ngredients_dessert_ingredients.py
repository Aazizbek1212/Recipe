# Generated by Django 5.0.7 on 2024-07-29 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_dessert_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dessert',
            old_name='ngredients',
            new_name='ingredients',
        ),
    ]
