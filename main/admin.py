from django.contrib import admin

from main.models import About, Cauntry, Dessert, Ingredient, Recipe, Review

# Register your models here.

admin.site.register(Cauntry)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Dessert)
admin.site.register(About)