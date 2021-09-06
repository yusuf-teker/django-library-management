
from library.views.bookDetail import bookDetail
from library.views.category import category
from django.urls import path,include
from library.views import homepage,myBooks,contact,ContactFormView
from django.views.generic import TemplateView, RedirectView 
urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('myBooks', myBooks, name='myBooks'),
    path('bookDetail/<slug:slug>', bookDetail,name='bookDetail'),
    path('contact' , ContactFormView.as_view(), name='contact'),
    
] 
