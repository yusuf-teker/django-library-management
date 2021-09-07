
from library.views.bookDetail import bookDetail
from library.views.category import category
from django.urls import path,include
from library.views import homepage,myBooks,contact,ContactFormView, add_book, update_book,delete_book, give_or_return_book
from django.views.generic import TemplateView, RedirectView 
urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myBooks', myBooks, name='myBooks'),
    path('bookDetail/<slug:slug>', bookDetail,name='bookDetail'),
    path('contact' , ContactFormView.as_view(), name='contact'),
    path('add-book' , add_book, name='add-book'),
    path('update-book/<slug:slug>' , update_book, name='update-book'),
    path('delete-book/<slug:slug>', delete_book, name='delete-book'),
    path('give-or-return-book/<slug:slug>', give_or_return_book, name='give-or-return-book'),
    
] 
