from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request,*args,**kwargs):
   # return HttpResponse("<h1> Hello world</h1>")
   return render(request,"home1.html",{})

def about_view(request,*args,**kwargs):
   # return HttpResponse("<h1> Hello world</h1>")
   my_context = {
         "title" : "This is about us",
         "my_number": 235,
         "my_list" :[23,67,78,"Abc"]

      }
   return render(request,"about.html",my_context)

def contact_view(request,*args,**kwargs):
    # return HttpResponse("<h1> This is contact page</h1>")
     return render(request,"contact.html",{})
