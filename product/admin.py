from django.contrib import admin

# Register your models here.
from .models import Product
#admin.site.register(Product)
class Pro(admin.ModelAdmin):
    list_display = ('title','description','price','quantity')
    list_filter  =['title']
    search_fields =['title']
    list_per_page = 1
admin.site.register(Product,Pro)
