from django.contrib import admin
from django.urls import path, include

# STATIC AND MEDIA FILES IMPORTs
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
]

# STATIC AND MEDIA FILES URLs
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)