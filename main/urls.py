from django.urls import path


from main.views import Desserts, Foods, about_view, cauntry_view, dessert_detail_view, detail_view, home_view, recipe_view


urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('allfoods/', Foods.as_view(), name='allfoods'),
    path('cauntry/', cauntry_view, name='cauntry'),
    path('recipes/<int:pk>', recipe_view, name='recipe'),
    path('dessert/', Desserts.as_view(), name='alldessert'),
    path('dessert/detail/<int:pk>/', dessert_detail_view, name='dessertdetail'),
    path('about/', about_view, name='about'),
    
]
