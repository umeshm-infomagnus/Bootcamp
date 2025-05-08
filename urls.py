from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_exoplanet, name='create_exoplanet'),
    path('read/', views.read_exoplanets, name='read_exoplanets'),
    path('update/<int:pk>/', views.update_exoplanet, name='update_exoplanet'),
    path('delete/<int:pk>/', views.delete_exoplanet, name='delete_exoplanet'),
]