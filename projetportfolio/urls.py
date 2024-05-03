from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("backoffice/", views.backoffice, name='backoffice' ),
    path("backoffice/edit/", views.edit_about, name="edit_about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

