# Generated by Django 5.0.7 on 2024-07-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
