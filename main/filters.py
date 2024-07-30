from django_filters import FilterSet

from main.models import Dessert, Recipe



class RecipeFilter(FilterSet):

    class Meta:
        model = Recipe
        fields = {'name':['contains']}



class DessertFilter(FilterSet):

    class Meta:
        model = Dessert
        fields = {'name':['contains']}



