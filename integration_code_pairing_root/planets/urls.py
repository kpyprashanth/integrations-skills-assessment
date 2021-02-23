from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.get_by_id),
    path('limit/<int:population_limit>', views.get_planet_above_population),
    path('<int:id>/?q=imperial', views.get_by_id_imperial),
]