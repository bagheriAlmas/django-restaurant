from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from almas_restaurant import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foods.urls')),
    path('', include('reservations.urls')),
    path('', include('blogs.urls')),

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('acounts/',include('django.contrib.auth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
