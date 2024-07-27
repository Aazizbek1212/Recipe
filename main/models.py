from django.db import models


class Cauntry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.PositiveSmallIntegerField(blank=True, null=True)

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
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=200)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name

