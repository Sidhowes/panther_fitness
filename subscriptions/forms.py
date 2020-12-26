from django import forms
from .models import Programme


class ProgrammeForm(forms.ModelForm):

    class Meta:
        model = Programme
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        programme = Programme.objects.all()