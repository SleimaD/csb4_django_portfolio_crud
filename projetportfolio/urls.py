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
    path("backoffice/new/", views.skill_add, name="skill_add"),
    path("backoffice/<int:id>/destroy/", views.delete_skill, name="delete_skill"),
    path("portfolio-details/", views.portfolio_details, name="portfolio-details"),
    path("backoffice/addproject/", views.add_project, name="add_project"),
    path("project/<int:id>/destroy/", views.delete_project, name="delete_project"),
    path("backoffice/addservice/", views.add_service, name="add_service"),
    path("service/<int:id>/destroy/", views.delete_service, name="delete_service")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



