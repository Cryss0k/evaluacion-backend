from django.urls import path
from . import views

urlpatterns = [
    path('vista1/', views.vista_uno, name='vista_uno'),
    path('vista2/', views.vista_dos, name='vista_dos'),
]