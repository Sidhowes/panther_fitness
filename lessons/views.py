from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Lesson
from .forms import LessonProgrammeForm


def lesson(request):
    """ A view to show all subscription lessons available to purchase """

    lessons = Lesson.objects.all()
    context = {
        'lessons': lessons,
    }
    return render(request, 'lessons/lessons.html', context)


def get_lesson_id(request, fitness_id):
    lesson_id = get_object_or_404(Lesson, pk=lesson_id)
    context = {
        'lesson_id': lesson_id,
      }

    return render(request, 'lessons/edit_lesson.html', context)


@login_required
def edit_lesson(request, lesson_id):
    """ Edit a lesson in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit a fitness lesson.')
        return redirect(reverse('home'))

    lesson_id = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LesssonProgrammeForm(request.POST, request.FILES, instance=lesson_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated fitness lesson details!')
            return redirect(reverse('lesson'))
        else:
            messages.error(request, 'Failed to update fitness lesson. Please ensure the form is valid.')
    else:
        form = LessonProgrammeForm(instance=lesson_id)

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson_id': lesson_id,
    }

    return render(request, template, context)
