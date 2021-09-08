
from library.views.bookDetail import BookDetailView
from library.views.category import CategoryListView
from django.urls import path,include
from library.views import homepage,myBooks,contact,ContactFormView, add_book, UpdateBookUpdateView,DeleteBookDeleteView, give_or_return_book,AddBookCreateView,CategoryListView
from django.views.generic import TemplateView, RedirectView 
urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<slug:categorySlug>', CategoryListView.as_view(), name='category'),
    path('myBooks', myBooks, name='myBooks'),
    path('bookDetail/<slug:slug>', BookDetailView.as_view(),name='bookDetail'),
    path('contact' , ContactFormView.as_view(), name='contact'),
    path('add-book' , AddBookCreateView.as_view(), name='add-book'),
    path('update-book/<slug:slug>' , UpdateBookUpdateView.as_view(), name='update-book'),
    path('delete-book/<slug:slug>', DeleteBookDeleteView.as_view(), name='delete-book'),
    path('give-or-return-book/<slug:slug>', give_or_return_book, name='give-or-return-book'),
    
] 
    