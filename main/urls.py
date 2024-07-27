from django.urls import path

from main.views import Foods, detail_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('allfoods/', Foods.as_view(), name='allfoods'),
]
