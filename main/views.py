from django.shortcuts import render

from django_filters.views import FilterView

from main.filters import RecipeFilter
from main.models import Ingredient, Recipe

def home_view(request):
    foods = Recipe.objects.all()[:4]
    return render(request, 'index.html', {'foods':foods})



def detail_view(request, pk):
    recipe = Recipe.objects.get(id=pk)
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