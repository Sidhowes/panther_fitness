from products.views import check_user
from .models import Programme
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def subscription_programme(request):
    """ A view to show all subscription programmes available to purchase """

    subscriptions = Programme.objects.all()
    has_programme = check_user(request)

    context = {
        'subscriptions': subscriptions,
        'has_programme': has_programme,
    }
    return render(request, 'subscriptions/subscriptions.html', context)

