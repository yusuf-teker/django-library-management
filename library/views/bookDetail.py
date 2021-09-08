from django.shortcuts import get_object_or_404, render
from library.models import BooksModel
from django.views import View

class BookDetailView(View):
    http_method_names = ['get']
    
    def get(self, request, slug):
        book = get_object_or_404(BooksModel,slug=slug)

        return render(request, 'pages/bookDetail.html',context={
        'book': book,
    } )
 
""" def bookDetail(request, slug):
    book = get_object_or_404(BooksModel,slug=slug)
    return render(request, 'pages/bookDetail.html',context={
        'book': book,
    } )

 """
