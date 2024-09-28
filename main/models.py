from django.db import models


class Cauntry(models.Model):
    image = models.ImageField(upload_to='iamges/cauntry/', blank=True, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    description = models.TextField(blank=True, null=True,)
    rating = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    prep = models.IntegerField()
    cook = models.IntegerField()
    yields = models.PositiveIntegerField()
    country = models.ForeignKey(Cauntry, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    rating = models.FloatField(blank=True, null=True, default=0.0)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True, null=True)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    foods = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='review', blank=True, null=True)

    def __str__(self):
        return self.name
