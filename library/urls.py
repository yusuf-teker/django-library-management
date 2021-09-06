from library.views.category import category
from django.urls import path,include
from library.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<slug:categorySlug>', category, name='category')

] 
