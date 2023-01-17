from django import forms

class ContactForm(forms.Form):
    email_address = forms.CharField(widget= forms.EmailInput())
    subject = forms.CharField(widget= forms.TextInput())
    message = forms.CharField(widget= forms.Textarea())

