from django.db import models

class ContactModel(models.Model):
    email = models.EmailField(max_length=200)
    name_surname = models.CharField(max_length=150)
    message = models.TextField()
    dateOfCreation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact'
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


    def __str__(self):
        return self.email 