
from django.urls import path

from .views import ProgrameListView, ProgrameDetailView

app_name = 'programes'

urlpatterns = [
    path('', ProgrameListView.as_view(), name='list'),
    path('<slug>', ProgrameDetailView.as_view(), name='detail')
]