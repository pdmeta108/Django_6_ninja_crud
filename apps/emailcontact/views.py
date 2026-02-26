from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
import os

from .forms import ContactForm

def success_view(request):
    """Obtener vista de envio de correo exitoso

    Parameters
    ----------
    request : request
        HTTP Request

    Returns
    -------
    render
        vista de exito
    """
    template_name = "emailcontact/success.html"
    return render(request, template_name)

def contact_view(request):
    """Obtener vista de formulario de contacto

    Parameters
    ----------
    request : request
        HTTP Request

    Returns
    -------
    render
        vista de formulario o redireccion a vista de exito
    """
    template_name = "emailcontact/contact.html"
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form_valid(form)
            # After successful POST, redirect to a new URL to prevent double submission
            return redirect('success')
    else:
        # If it's a GET request, create an empty form instance to display
        form = ContactForm()
    # Render the template with the form
    return render(request, template_name, {'form': form})

def form_valid(form):
    """Enviar mensaje de correo por consola o servidor SMTP

    Parameters
    ----------
    form : ContactForm
        Objeto para manipular datos del formulario de contacto
    """
    email = form.cleaned_data.get("email")
    subject = form.cleaned_data.get("subject")
    message = form.cleaned_data.get("message")

    # Usar metodo send_mail para enviar correos simples
    # full_message = f"""
    #     Received message below from {email}, {subject}
    #     ________________________


    #     {message}
    #     """
    # send_mail(
    #     subject="Received contact form submission",
    #     message=full_message,
    #     from_email=settings.DEFAULT_FROM_EMAIL,
    #     recipient_list=[settings.NOTIFY_EMAIL],
    #     fail_silently=False,
    # )

    # Crear objeto email con formato html y una imagen atada al correo y enviar
    full_message="<div><h2>Mensaje formato HTML con imagen</h2><p>" + email + ", " + subject + "</p><p>" + message + "</p></div>"

    email = EmailMessage(
            subject='Test Email with Attachment from Django',
            body=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.NOTIFY_EMAIL],
        )
    email.content_subtype = "html"

    file_path = os.path.join(settings.BASE_DIR, 'apps/emailcontact/assets/doge.png')
    email.attach_file(file_path)

    email.send(fail_silently=False)
