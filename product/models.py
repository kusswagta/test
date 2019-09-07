from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    quantity    = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)

    
