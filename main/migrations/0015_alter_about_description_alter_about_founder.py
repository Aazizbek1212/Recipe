# Generated by Django 5.0.7 on 2024-07-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='founder',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
