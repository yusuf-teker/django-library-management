from library.models.contact import ContactModel
from library.models.books import BooksModel
from library.models.categories import CategoriesModel
from django.contrib import admin
from library.models.photo import PhotoModel

# Register your models here.

admin.site.register(CategoriesModel)

class BooksAdmin(admin.ModelAdmin):
    search_fields= ('bookName','categories' , 'publicationYear')
    list_displays = {
        'bookName','categories' , 'publicationYear'
    }

admin.site.register(BooksModel)
admin.site.register(ContactModel
)

class PhotoAdmin(admin.ModelAdmin):
    search_fields= ('file','description' , 'uploaded_at')
    list_displays = {
        'file','description' , 'uploaded_at'
    }
admin.site.register(PhotoModel,PhotoAdmin)
#class ContactAdmin(admin.ModelAdmin):
#    list_display = {'name_surname','dateOfCreation'}
#    search_fields= ('email')

#admin.site.register(ContactModel,ContactAdmin)
