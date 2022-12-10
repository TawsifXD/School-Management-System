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
    path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT, name="view_student" ),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT, name="edit_student" ),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT, name="update_student" ),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT, name="delete_student" ),

    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:id>',Hod_Views.DELETE_STAFF,name='delete_staff'),

    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),

    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name='add_subject'),
    # path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),
    # path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
    # path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
    # path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
