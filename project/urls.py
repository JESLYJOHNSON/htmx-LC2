# urls.py

from django.contrib import admin
from django.urls import path
from app.views import index, search, export_csv 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('search/', search, name="search"),
    path('export-csv/', export_csv, name='export_csv'),
    
]


