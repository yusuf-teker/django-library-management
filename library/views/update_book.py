from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from library import forms
from library.forms import UpdateBookModelForm
from library.models import BooksModel
from django.views.generic import UpdateView
from django.urls import reverse
""" @login_required(login_url='/')
def update_book(request, slug):
    book = get_object_or_404(BooksModel, slug=slug)
    form = UpdateBookModelForm(request.POST or None, files=request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('bookDetail', slug = book.slug)
    return render(request, 'pages/update-book.html', context={'form':form})
 """
class UpdateBookUpdateView( UpdateView):
    template_name = 'pages/update-book.html'
    fields = ('bookName', 'author', 'coverPicture', 'categories','bookBlurb','numberOfPages','publicationYear')

    def get_object(self):
        if not (self.request.user.groups.filter(name__in=['officer', 'admin']).exists()):
            return redirect('/')
        book = get_object_or_404(
            BooksModel,
            slug=self.kwargs.get('slug'),)
        return book
    
    def get_success_url(self):
        if not (self.request.user.groups.filter(name__in=['officer', 'admin']).exists()):
            return redirect('/')
        return reverse('bookDetail', kwargs={
            'slug': self.get_object().slug
        })