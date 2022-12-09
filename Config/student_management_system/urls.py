from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views, Staff_Views, Hod_Views, Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login From
    path('', views.LOGIN, name='login'),
    path('dologin', views.doLogin, name='doLogin'),
    path('dologout', views.doLogout, name='Logout'),

    # Profile Update
    path('profile', views.PROFILE, name= 'profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # Head Of Department Penal Url
    path('Hod/home', Hod_Views.HOME, name='hod_home'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
