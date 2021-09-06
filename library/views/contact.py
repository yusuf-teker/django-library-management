from django import forms
from django.shortcuts import redirect, render

from library.forms import ContactForm 
from library.models import ContactModel  

from django.views.generic import FormView


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/'  #işlem başarılıysa ne yapılacak
        #url kısmında templateview ile path ekle
    def form_valid(self,form):
        form.save()
        form.send_email(message= form.cleaned_data.get('message'))
        return redirect(self.success_url)

