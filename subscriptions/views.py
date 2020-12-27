from django.shortcuts import render
from .models import Programme



def subscription_programme(request):
    """ A view to show all subscription programmes available to purchase """

    subscriptions = Programme.objects.all()
    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'subscriptions/subscriptions.html', context)
