from django.contrib import admin

from main.models import Cauntry, Ingredient, Recipe, Review

# Register your models here.

admin.site.register(Cauntry)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Review)