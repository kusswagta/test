from django.urls import path
from .import views
from mysite import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.create_profile, name = 'create'),
]
