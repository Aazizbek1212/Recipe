# Generated by Django 5.0.7 on 2024-07-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_ingredient_quantity_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
