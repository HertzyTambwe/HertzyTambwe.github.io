
from django.contrib import admin
from django.urls import path

from portfolio.views import index, my_projets

urlpatterns = [
    path('', index, name='index'),
    path('projets/', my_projets, name='my-projets'),
    path('admin/', admin.site.urls),
]
