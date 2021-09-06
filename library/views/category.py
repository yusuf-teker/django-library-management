from django.shortcuts import render, get_object_or_404
from library.models import BooksModel,CategoriesModel
from django.core.paginator import Paginator
# Create your views here.
def category(request, categorySlug):
    
    category = get_object_or_404(CategoriesModel, slug= categorySlug)
    books = category.book.order_by('-id')
   
    page = request.GET.get('page')
    paginator = Paginator(books,2)

    return render(request,'pages/category.html',context={
        'books': paginator.get_page(page),
        'categoryName' : category.categoryName
    })