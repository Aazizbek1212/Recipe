from django_filters import FilterSet

from main.models import Recipe



class RecipeFilter(FilterSet):

    class Meta:
        model = Recipe
        fields = {'name':['contains']}
