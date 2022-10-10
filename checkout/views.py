from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Lg4huGqEN8R8NzsPaNJkJJK3wxZ6w5X3i6SJt56u08srBodLh6DmtQK2wvZ2mhtTUThiFAsnKLljmWHGeq2cjjc0030iUdNXY',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
