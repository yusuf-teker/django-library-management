from django.shortcuts import get_object_or_404, render
from library.models import BooksModel
def bookDetail(request, slug):
    book = get_object_or_404(BooksModel,slug=slug)
    return render(request, 'pages/bookDetail.html',context={
        'book': book,
    } )


