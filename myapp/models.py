from django.db import models

# Create your models here.
class Myapp(models.Model):
    title = models.TextField()
    fname = models.TextField()


