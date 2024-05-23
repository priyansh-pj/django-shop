from django.contrib import admin
from django.urls import path, include
# for image
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('owner.urls')),
    path('', include('inventory.urls')),
    path('account/', include('account.urls')),
]
# for image upload for permission
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)