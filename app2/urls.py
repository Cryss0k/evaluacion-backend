from django.urls import path
from . import views

urlpatterns = [
    path('vista3/', views.vista_tres, name='vista_tres'),
    path('vista4/', views.vista_cuatro, name='vista_cuatro'),
]