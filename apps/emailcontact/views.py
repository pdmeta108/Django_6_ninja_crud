from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, reverse

from .forms import ContactForm


def success_view(request):
    template_name = "emailcontact/success.html"
    return render(request, template_name)


def get_success_url():
    return reverse("contact")

def contact_view(request):
    template_name = "emailcontact/contact.html"
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form_valid(form)
            # After successful POST, redirect to a new URL to prevent double submission
            return redirect('person:home')
    else:
        # If it's a GET request, create an empty form instance to display
        form = ContactForm()
    # Render the template with the form
    return render(request, template_name, {'form': form})


def form_valid(form):
    email = form.cleaned_data.get("email")
    subject = form.cleaned_data.get("subject")
    message = form.cleaned_data.get("message")

    full_message = f"""
        Received message below from {email}, {subject}
        ________________________


        {message}
        """
    send_mail(
        subject="Received contact form submission",
        message=full_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.NOTIFY_EMAIL],
    )
