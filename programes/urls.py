
from django.urls import path

from .views import ProgrameListView, ProgrameDetailView, LessonDetailView

app_name = 'programes'

urlpatterns = [
    path('', ProgrameListView.as_view(), name='list'),
    path('<slug>', ProgrameDetailView.as_view(), name='detail'),
    path('<programe_slug>/<lesson_slug>', LessonDetailView.as_view(), name='lesson_detail')
]