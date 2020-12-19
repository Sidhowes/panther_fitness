from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Programe


class ProgrameListView(ListView):
    model = Programe


class ProgrameDetailView(DetailView):
    model = Programe
