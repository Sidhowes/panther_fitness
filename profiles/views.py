from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from lessons.views import lesson
from .models import UserProfile
from products.views import check_user
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed, ensure form is valid')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    for order in orders:
        line_items = order.lineitems.all()
        for item in line_items :
            print(item.product.name)

    # call lesson func from lesson.views
    lesson(request)
    has_programme = check_user(request)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'has_programme': has_programme,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)