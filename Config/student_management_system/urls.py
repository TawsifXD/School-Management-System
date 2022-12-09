from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views, Staff_Views, Hod_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login From
    path('login/', views.LOGIN, name='login'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
