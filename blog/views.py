from django.shortcuts import render
# Create your views here.
from .forms import BlogForm
from .models import Blog
def blog_create_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
       form.save()
    context = {
        'form':form,
       }
    return render(request,"blog/blog_create.html",context)
def blog_fetch_view(request):
   posts = Blog.objects.all()
   
   args = {
        'posts':posts
     }
   return render(request,"blog/blog_fetch.html",args)
def blog_detail_view(request):
   obj = Blog.objects.get(id=1)
   context = {
        'title':obj.title,
        'description' :obj.description
   }
   return render(request,"blog/blog_detail.html",context)
def blog_home_view(request):
   # return HttpResponse("<h1> Hello world</h1>")
   return render(request,"blog/blog_home.html",{})

def blog_contact_view(request):
  
  return render(request,"blog/blog_contact.html",{})

