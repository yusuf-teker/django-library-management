
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from library.models import BooksModel
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy 
@login_required(login_url='/')
def delete_book(request,slug):
    get_object_or_404(BooksModel,slug=slug).delete()
    return redirect('/')

class DeleteBookDeleteView(DeleteView):
    
    
    
    template_name = 'pages/delete_book_confirmation.html'
    success_url = reverse_lazy('homepage')


    def get_queryset(self):
        # if not (self.request.user.groups.filter(name = 'admin').exists()):
        #        return redirect('/') 
        book = BooksModel.objects.filter(slug = self.kwargs['slug'])
        return book