from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    title       =RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return '{}'.format(self.title)
