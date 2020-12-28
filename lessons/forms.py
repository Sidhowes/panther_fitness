from django import forms
from .models import Lesson


class LessonProgrammeForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lesson_form = Lesson.objects.all()