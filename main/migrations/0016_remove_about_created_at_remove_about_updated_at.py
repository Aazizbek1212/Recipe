# Generated by Django 5.0.7 on 2024-07-29 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_about_description_alter_about_founder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='about',
            name='updated_at',
        ),
    ]
