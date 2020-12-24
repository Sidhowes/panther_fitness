from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_programme, name='subscription_programme'),
]