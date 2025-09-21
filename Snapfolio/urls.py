# Snapfolio/urls.py (main project file)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Snapfolio.urls')), # This connects the app
]