from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FitnessProgrammeForm
from .models import Fitness


def fitness(request):
    fitness_obj = Fitness.objects.all()

    template = 'fitness/fitness.html'

    context = {
        'fitness_obj': fitness_obj,
    }

    return render(request, template, context)


def get_fitness_id(request, fitness_id):
    fitness_id = get_object_or_404(Fitness, pk=fitness_id)
    context = {
        'fitness_id': fitness_id,
      }

    return render(request, 'fitness/edit_fitness_lesson.html', context)


@login_required
def edit_fitness_lesson(request, fitness_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit a fitness lesson.')
        return redirect(reverse('home'))

    fitness_id = get_object_or_404(Fitness, pk=fitness_id)
    if request.method == 'POST':
        form = FitnessProgrammeForm(request.POST, request.FILES, instance=fitness_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated fitness lesson details!')
            return redirect(reverse('fitness'))
        else:
            messages.error(request, 'Failed to update fitness lesson. Please ensure the form is valid.')
    else:
        form = FitnessProgrammeForm(instance=fitness_id)

    template = 'fitness/edit_fitness_lesson.html'
    context = {
        'form': form,
        'fitness.id': fitness.id,
    }

    return render(request, template, context)