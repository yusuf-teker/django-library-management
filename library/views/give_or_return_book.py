from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from library import forms
from library.forms import GiveOrReturnBookModelForm
from library.models import BooksModel

@login_required(login_url='/')
def give_or_return_book(request, slug):
    if not request.user.groups.filter(name__in=['officer', 'admin']).exists():
        return redirect('/')
    book = get_object_or_404(BooksModel, slug=slug)
    form = GiveOrReturnBookModelForm(request.POST or None, files=request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('bookDetail', slug = book.slug)
    return render(request, 'pages/give-or-return-book.html', context={'form':form})