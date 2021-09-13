from django import forms
from library.models import BooksModel,CategoriesModel


class AddBookModelForm(forms.ModelForm):
    class Meta:
        model = BooksModel
        exclude = ('lendby','lendperiod','isAvailable','slug')
