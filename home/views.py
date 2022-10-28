from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page and recent products """
    products = Product.objects.all().order_by('-added_on')[:3]

    context = {'products': products}

    return render(request, 'home/index.html', context)


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')
