from django.contrib import admin

# Register your models here.
from .models import Blog
#admin.site.register(Blog)
class BlogListing(admin.ModelAdmin):
    
     list_display = ('title','description')
     list_filter =['title']
     search_fields =['title']
     list_per_page = 1
admin.site.register(Blog,BlogListing)
