from django.shortcuts import get_object_or_404,  render

from django_filters.views import FilterView

from main.filters import DessertFilter, RecipeFilter
from main.models import About, Cauntry, Dessert, Ingredient, Recipe, Review

def home_view(request):
    foods = Recipe.objects.all()[:3]
    food = Recipe.objects.all()[:6]
    return render(request, 'index.html', {'foods':foods, 'food':food})



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


class Desserts(FilterView):
    model = Dessert
    template_name = 'dessert.html'
    context_object_name = 'desserts'
    filterset_class = DessertFilter

    def get_queryset(self):
        i = super().get_queryset()
        search = self.request.GET.get('DessertSearch', None)
        
        if search:
            i = i.filter(name__contains=search)
        return i


def dessert_detail_view(request, pk):
    dessert = get_object_or_404(Dessert, id=pk)
    return render(request, 'dessertdetail.html', {'dessert':dessert})


def about_view(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about':about})


