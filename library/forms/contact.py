from django import forms
from django.forms import fields
from library.models import ContactModel
from django.core.mail import send_mail


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = ('name_surname', 'email', 'message')
    
    def send_email(self,message):
        send_mail(
            subject="Contact",
            message=message,
            from_email=None,
            recipient_list=['y.teker.1907@gmail.com'],
            fail_silently=False)