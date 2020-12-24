from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness, name='fitness'),
    path('<int:nfitness_id>/', views.get_fitness_id,
        name='get_fitness_id'),
]