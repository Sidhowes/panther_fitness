from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Fitness

def fitness(request):
    fitness_obj = Fitness.objects.all()

    template = 'fitness/ftness.html'

    context = {
        'fitness_obj': fitness_obj,
    }

    return render(request, template, context)


def get_fitness_id(request, nutrition_id):
    fitness_id = get_object_or_404(Fitness, pk=fitness_id)
    context = {
        'fitness_id': fitness_id,
      }

    return render(request, 'fitness/edit_fitness.html', context)

