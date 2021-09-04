from django.db import models
from autoslug import AutoSlugField
from library.models import CategoriesModel

class BooksModel(models.Model):
    bookName = models.CharField(max_length=50,blank=False,null=False)
    slug = AutoSlugField(populate_from = 'bookName', unique=True)
    bookBlurb = models.TextField()
    categories = models.ManyToManyField(CategoriesModel, related_name='book')
    coverPicture = models.ImageField(upload_to='book_cover_picture')
    author = models.CharField(max_length=30)
    numberOfPages = models.IntegerField()
    publicationYear = models.DateField()
    
    class Meta:
        db_table = 'book'

    def __str__(self) :
        return self.bookName