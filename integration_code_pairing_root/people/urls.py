from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.get_by_id),
    path('height_less_than/<int:height_upper_limit>', views.get_people_less_than_height),
    path('eye_color/<str:eye_color>', views.get_people_with_eye_color)
]