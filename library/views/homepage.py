from django.shortcuts import render
from library.models import BooksModel
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def homepage(request):
    query = request.GET.get('query')
    books = BooksModel.objects.all()

    if query:
        books = books.filter(
            Q(bookName__icontains = query) |
            Q(id__icontains = query)
        ).distinct() 

    page = request.GET.get('page')
    paginator = Paginator(books,2)
    return render(request,'pages/homepage.html',context={
        'books': paginator.get_page(page)
    })

