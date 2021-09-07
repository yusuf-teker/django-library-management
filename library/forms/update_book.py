from django import forms
from django.forms import fields
from library.models import BooksModel



class UpdateBookModelForm(forms.ModelForm):

    class Meta:
        model = BooksModel
        exclude = ('slug','isAvailable', 'lendby', 'lendperiod')
    
  