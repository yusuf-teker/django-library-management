from django.db import models
from autoslug import AutoSlugField
from library.models import CategoriesModel
from django.contrib.auth.models import User
import os
from uuid import uuid4
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.bookName:
            filename = '{}.{}'.format(instance.bookName, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class BooksModel(models.Model):
   
    bookName = models.CharField(max_length=50,blank=False,null=False)
    slug = AutoSlugField(populate_from = 'bookName', unique=True)
    bookBlurb = models.TextField()
    categories = models.ManyToManyField(CategoriesModel, related_name='book')
    #coverPicture = models.ImageField(upload_to='book_cover_picture')
    coverPicture = models.ImageField(upload_to=path_and_rename('book_cover_picture'))
    author = models.CharField(max_length=30)
    numberOfPages = models.IntegerField()
    publicationYear = models.DateField()
    isAvailable = models.BooleanField(default=True)
    #isAvailable = models.BooleanField(default=True)
    lendby = models.ForeignKey(User , blank=True, null=True, on_delete=models.CASCADE,related_name='books')
    lendperiod = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'book'

    def __str__(self) :
        return self.bookName
    
