from django.db import models

class PhotoModel(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'