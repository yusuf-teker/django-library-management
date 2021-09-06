from django.shortcuts import render
from library.models import BooksModel
from django.core.paginator import Paginator
# Create your views here.
def homepage(request):
    books = BooksModel.objects.all()

    page = request.GET.get('page')
    paginator = Paginator(books,2)
    return render(request,'pages/homepage.html',context={
        'books': paginator.get_page(page)
    })