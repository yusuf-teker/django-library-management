from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from library import forms
from library.forms import AddBookModelForm

@login_required(login_url='/')
def add_book(request):
    form = AddBookModelForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        book = form.save()
  
        return redirect('bookDetail', slug=book.slug) 
    return render(request, 'pages/add-book.html', context={'form':form})