from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_us(request):
    if request.method == 'POST':
        # Submit The Form.
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # If The Form is Valid, Get The Filled Data From The Form Fields.
            email_address = contact_form.cleaned_data.get('email_address')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')

            try:
                # Try to Send The Email Message.
                send_mail(
                    subject = subject,
                    message= message,
                    from_email= email_address,
                    recipient_list= [settings.EMAIL_HOST_USER],
                    fail_silently= False
                )
            
            # If The Email subject, from_email and recipient_list aren't properly formatted, Raise an Error Message and Don't Send The Email.
            except BadHeaderError:
                messages.error(request, 'Invalid Header Found.')
                return redirect('contact')

            # If The Email is Sent or There's an Error, Back to The Home Page.
            return redirect('home')
        
    else:
        # Display The Blank Form.
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(
        request= request,
        template_name= 'contact/contact.html',
        context = context
    )