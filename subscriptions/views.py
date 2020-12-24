from django.shortcuts import render
from .models import Programme
from products.views import check_user


def subscription_programme(request):
    """ A view to show all subscription programmes available to purchase """

    subscriptions = Programme.objects.all()
    has_programme = check_user(request)
    context = {
        'subscriptions': subscriptions,
        'has_programme': has_programme,
    }
    return render(request, 'subscriptions/subscriptions.html', context)


