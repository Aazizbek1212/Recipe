from django.shortcuts import get_object_or_404, render

from django_filters.views import FilterView

from main.filters import RecipeFilter
from main.models import Cauntry, Dessert, Ingredient, Recipe

def home_view(request):
    foods = Recipe.objects.all()[:4]
    return render(request, 'index.html', {'foods':foods})



def detail_view(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    return render(request, 'detail.html', {'recipe':recipe})


class Foods(FilterView):
    model = Recipe
    template_name = 'all_foods.html'
    context_object_name = 'foods'
    filterset_class = RecipeFilter

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('Search', None)
        
        if search:
            qs = qs.filter(name__contains=search)
        return qs
    


def cauntry_view(request):
    cauntry = Cauntry.objects.all()
    return render(request, 'cauntries.html', {'cauntry':cauntry})


def recipe_view(request, pk):
    destinations = Cauntry.objects.get(id=pk)
    recipe = destinations.recipe_set.all()
    return render(request, 'cauntry_foods.html', {'destinations':destinations, 'recipe':recipe})


def dessert_view(request):
    desserts = Dessert.objects.all()
    return render(request, 'dessert.html', {'desserts':desserts})