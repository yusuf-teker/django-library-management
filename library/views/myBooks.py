from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.   
from django.contrib.auth.decorators import login_required
from library.models import BooksModel

@login_required(login_url='/')
def myBooks (request):
    
    books = BooksModel.objects.filter(lendby = request.user)
   # books = request.user.books.order_by('-id')
   
    page = request.GET.get('page')
    paginator = Paginator(books,2)

    return render(request,'pages/myBooks.html',context={
        'books': paginator.get_page(page),
    
    })