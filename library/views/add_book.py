from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls.base import reverse,reverse_lazy
from library.forms import AddBookModelForm
from django.views.generic import CreateView
from library.models import BooksModel, categories,CategoriesModel

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
class   AddBookCreateView(LoginRequiredMixin,CreateView):
    
    login_url = reverse_lazy('login')
    template_name = 'pages/add-book.html'
    model = BooksModel
    fields=('bookName','bookBlurb', 'categories','coverPicture','author','numberOfPages','publicationYear')

   
    def form_valid(self, form):
        if not (self.request.user.groups.filter(name = 'admin').exists()):
            return redirect('/')
            
        book = form.save(commit = False)  
        book.save()
        return super().form_valid(form)

    def get_success_url(self): 
        return reverse('bookDetail', kwargs={
            'slug': self.object.slug
        })
    
