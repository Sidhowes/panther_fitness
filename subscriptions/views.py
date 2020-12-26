from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Programme
from products.views import check_user
from .forms import ProgrammeForm



def subscription_programme(request):
    """ A view to show all subscription programmes available to purchase """

    subscriptions = Programme.objects.all()
    has_programme = check_user(request)
    context = {
        'subscriptions': subscriptions,
        'has_programme': has_programme,
    }
    return render(request, 'subscriptions/subscriptions.html', context)


def get_programme_id(request, programme_id):
    programme_id = get_object_or_404(Programme, pk=programme_id)
    context = {
        'programme_id': programme_id,
    }

    return render(request, 'subscriptions/edit_subscription.html',
                  context)



@login_required
def edit_subscription(request, programme_id):
    """ Edit a subscription programme """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit a programme.')
        return redirect(reverse('home'))

    programme = get_object_or_404(Programme, pk=programme_id)
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, request.FILES, instance=programme)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated programme!')
            return redirect(reverse('subscription_programme', args=[programme.id]))
        else:
            messages.error(request, 'Failed to update programme. Please ensure the form is valid.')
    else:
        form = ProgrammeForm(instance=programme)
        messages.info(request, f'You are editing {programme.programme_duration}')

    template = 'suscriptions/edit_subscription.html'
    context = {
        'form': form,
        'programme': programme,
    }

    return render(request, template, context)