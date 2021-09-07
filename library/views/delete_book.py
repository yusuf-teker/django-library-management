from django.contrib.auth.decorators import login_required
from library.models import BooksModel
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='/')
def delete_book(request,slug):
    get_object_or_404(BooksModel,slug=slug).delete()
    return redirect('/')
