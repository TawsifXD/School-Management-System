from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views, Staff_Views, Hod_Views, Student_Views

urlpatterns = [

    # --------------------------Website Links---------------------------
    path('', views.HOME, name='home'),
    path('about/', views.ABOUT, name='about'),
    path('course/', views.COURSE, name='course'),
    path('contact/', views.CONTACT, name='contact'),

    # ----------------------------DashBord Links-------------------------
    path('admin', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login From
    path('Login', views.LOGIN, name='login'),
    path('Dologin', views.doLogin, name='doLogin'),
    path('Dologout', views.doLogout, name='Logout'),

    # Profile Update
    path('Profile', views.PROFILE, name= 'profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

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
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),

    path('Hod/Session/Add',Hod_Views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',Hod_Views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_Views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',Hod_Views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_Views.DELETE_SESSION,name='delete_session'),

    path('Hod/Staff/Send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION, name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_Views.SAVE_STAFF_NOTIFICATION, name='save_staff_notification'),

    path('Hod/Student/Send_Notification',Hod_Views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('Hod/Student/Save_Notification',Hod_Views.SAVE_STUDENT_NOTIFICATION, name='save_student_notification'),

    path('Hod/Staff/Leave_view',Hod_Views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('Hod/Staff/Approve_leave/<str:id>',Hod_Views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Hod/Staff/Disapprove_leave/<str:id>',Hod_Views.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),

    path('Hod/Student/Leave_view',Hod_Views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('Hod/Student/Approve_leave/<str:id>',Hod_Views.STUDENT_APPROVE_LEAVE,name='student_approve_leave'),
    path('Hod/Student/Disapprove_leave/<str:id>',Hod_Views.STUDENT_DISAPPROVE_LEAVE,name='student_disapprove_leave'),

    path('Hod/Staff/Feedback',Hod_Views.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('Hod/Staff/Feedback/ Save',Hod_Views.STAFF_FEEDBACK_SAVE,name='staff_feedback_reply_save'),

    path('Hod/Student/Feedback',Hod_Views.STUDENT_FEEDBACK,name='student_feedback_reply'),
    path('Hod/Student/Feedback/ Save',Hod_Views.REPLY_STUDENT_FEEDBACK,name='reply_student_feedback'),

    path('Hod/View/Attendance',Hod_Views.VIEW_ATTENDANCE,name='view_attendance'),

    # --------------------------Staff Penal Url --------------------------------

    path('Staff/home', Staff_Views.HOME, name='staff_home'),

    path('Staff/Notifications', Staff_Views.NOTIFICATIONS, name='notifications'),
    path('Staff/Mark_as_done/<str:status>', Staff_Views.STAFF_NOTIFICATION_DONE, name='staff_notification_done'),

    path('Staff/Apply_leave', Staff_Views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('Staff/Apply_leave_save', Staff_Views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),

    path('Staff/Feedback', Staff_Views.STAFF_FEEDBACK, name='staff_feedback'),
    path('Staff/Feedback/Save', Staff_Views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

    path('Staff/Take_Attendance', Staff_Views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Staff/Save_Attendance', Staff_Views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Staff/View_Attendance', Staff_Views.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),

    path('Staff/Add/Result', Staff_Views.STAFF_ADD_RESULT, name= 'staff_add_result'),
    path('Staff/Save/Result', Staff_Views.STAFF_SAVE_RESULT, name= 'staff_save_result'),

 # --------------------------Student Penal Url --------------------------------

    path('Student/Home', Student_Views.HOME, name='student_home'),

    path('Student/Notifications', Student_Views.NOTIFICATIONS, name='student_notifications'),
    path('Student/Mark_as_done/<str:status>', Student_Views.STUDENT_NOTIFICATION_DONE, name='student_notification_done'),

    path('Student/Feedback', Student_Views.STUDENT_FEEDBACK, name='student_feedback'),
    path('Student/Feedback/Save', Student_Views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),

    path('Student/Apply_leave', Student_Views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('Student/Apply_leave_save', Student_Views.STUDENT_APPLY_LEAVE_SAVE, name='student_apply_leave_save'),

    path('Student/View_Attendance', Student_Views.STUDENT_VIEW_ATTENDANCE, name='student_view_attendance'),

    path('Student/View_Result', Student_Views.STUDENT_VIEW_RESULT, name='student_view_result'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
