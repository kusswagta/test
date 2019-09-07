"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from  pages import views
from pages.views import home_view,about_view,contact_view
from blog.views import blog_detail_view,blog_create_view,blog_fetch_view,blog_contact_view,blog_home_view
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('blog/', blog_home_view),
    path('contact/',blog_contact_view),
    path('about/',about_view),
    path('blog/',blog_detail_view),
    path('create/',blog_create_view),
    path('fetch/',blog_fetch_view),
    path('admin/', admin.site.urls),
    path('upload/', include('profile_maker.urls'))]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
