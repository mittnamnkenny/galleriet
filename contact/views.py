from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """ A view to return the contact page and form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message successfully sent.')
        else:
            messages.error(
                request,
                'Failed to send message. Please ensure the form is valid.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
