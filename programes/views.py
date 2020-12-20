from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from memberships.models import UserMembership
from .models import Programe, Lesson


class ProgrameListView(ListView):
    model = Programe


class ProgrameDetailView(DetailView):
    model = Programe


class LessonDetailView(LoginRequiredMixin, View):

    def get(self, request, programe_slug, lesson_slug, *args, **kwargs):
        programe = get_object_or_404(Programe, slug=programe_slug)
        lesson = get_object_or_404(Lesson, slug=lesson_slug)
        user_membership = get_object_or_404(UserMembership, user=request.user)
        user_membership_type = user_membership.membership.membership_type
        programe_allowed_mem_types = programe.allowed_memberships.all()
        context = {
            'object': None
        }
        if programe_allowed_mem_types.filter(
                membership_type=user_membership_type).exists():
            context = {
                'object': lesson
            }
        return render(request, "programes/lesson_detail.html", context)
