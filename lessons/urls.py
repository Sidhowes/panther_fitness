from django.urls import path
from . import views

urlpatterns = [
    path('', views.lesson, name='lesson'),
    path('<int:lesson_id>/', views.get_lesson_id, name='get_lesson_id'),
    path('edit_lesson/<int:lesson_id>', views.edit_lesson,
         name='edit_lesson'),
]