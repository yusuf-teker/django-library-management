from library.models.books import BooksModel
from library.models.categories import CategoriesModel
from django.contrib import admin

# Register your models here.

admin.site.register(CategoriesModel)

class BooksAdmin(admin.ModelAdmin):
    search_fields= ('bookName','categories' , 'publicationYear')
    list_displays = {
        'bookName','categories' , 'publicationYear'
    }

admin.site.register(BooksModel)
