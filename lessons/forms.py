from django import forms
from .models import Lesson
from .widgets import CustomClearableFileInput1


class LessonProgrammeForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lesson_form = Lesson.objects.all()
