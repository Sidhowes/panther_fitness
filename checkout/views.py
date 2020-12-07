from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HuzU9HwhHVU1WMUHE7DmAsVrBs0dC8QzikICKpSuepIichbqe2LsAmqmFuPkhq5CsU0G5uMHO1kf4gBkIHoddJ000Fk5n1onK',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
