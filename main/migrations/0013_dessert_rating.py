# Generated by Django 5.0.7 on 2024-07-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_ngredients_dessert_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]