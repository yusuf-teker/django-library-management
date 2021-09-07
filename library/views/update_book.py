from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from library import forms
from library.forms import UpdateBookModelForm
from library.models import BooksModel

@login_required(login_url='/')
def update_book(request, slug):
    book = get_object_or_404(BooksModel, slug=slug)
    form = UpdateBookModelForm(request.POST or None, files=request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('bookDetail', slug = book.slug)
    return render(request, 'pages/update-book.html', context={'form':form})