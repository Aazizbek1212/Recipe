from django.urls import path

from main.views import Foods, cauntry_view, detail_view, home_view, recipe_view


urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('allfoods/', Foods.as_view(), name='allfoods'),
    path('cauntry/', cauntry_view, name='cauntry'),
    path('recipes/<int:pk>', recipe_view, name='recipe'),
]
