# Snapfolio/urls.py (main project file)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Import this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Snapfolio.urls')),
]

# This is only for the development server
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)