# Generated by Django 5.0.7 on 2024-07-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_ingredient_quantity_alter_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cauntry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='iamges/cauntry/'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
