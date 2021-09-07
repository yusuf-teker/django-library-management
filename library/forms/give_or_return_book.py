from django import forms
from django.forms import fields
from library.models import BooksModel


class GiveOrReturnBookModelForm(forms.ModelForm):

    class Meta:
        model = BooksModel
        fields = ('isAvailable', 'lendby', 'lendperiod')
        
    
  