from django import forms
from .models import Fitness


class FitnessProgrammeForm(forms.ModelForm):

    class Meta:
        model = Fitness
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fitness_form = Fitness.objects.all()