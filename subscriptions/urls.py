from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscription_programme, name='subscription_programme'),
    path('<int:programme_id>/', views.get_programme_id, name='get_programme_id'),
    path('edit_subscription/<int:programme_id>',
         views.edit_subscription, name='edit_subscription')
]