
from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews


urlpatterns = [
    path('', views.loginPage, name="login"),

    #  path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),

    # admin staff
    path('add_staff/', HodViews.add_staff, name="add_staff"),
    path('add_staff_save/', HodViews.add_staff_save, name="add_staff_save"),
    path('manage_staff/', HodViews.manage_staff, name="manage_staff"),
    path('edit_staff/<staff_id>/', HodViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/', HodViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', HodViews.delete_staff, name="delete_staff"),

    # admin department
    path('add_department/', HodViews.add_department, name="add_department"),
    path('add_department_save/', HodViews.add_department_save, name="add_department_save"),
    path('manage_department/', HodViews.manage_department, name="manage_department"),
    path('edit_department/<department_id>/', HodViews.edit_department, name="edit_department"),
    path('edit_department_save/', HodViews.edit_department_save, name="edit_department_save"),
    path('delete_department/<department_id>/', HodViews.delete_department, name="delete_department"),

    # admin course
    path('add_course/', HodViews.add_course, name="add_course"),
    path('add_course_save/', HodViews.add_course_save, name="add_course_save"),
    path('manage_course/', HodViews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', HodViews.edit_course, name="edit_course"),
    path('edit_course_save/', HodViews.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', HodViews.delete_course, name="delete_course"),

    # admin session
    path('manage_session/', HodViews.manage_session, name="manage_session"),
    path('add_session/', HodViews.add_session, name="add_session"),
    path('add_session_save/', HodViews.add_session_save, name="add_session_save"),
    path('edit_session/<session_id>', HodViews.edit_session, name="edit_session"),
    path('edit_session_save/', HodViews.edit_session_save, name="edit_session_save"),
    path('delete_session/<session_id>/', HodViews.delete_session, name="delete_session"),

    # admin intake
    path('add_intake/', HodViews.add_intake, name="add_intake"),
    path('add_intake_save/', HodViews.add_intake_save, name="add_intake_save"),
    path('manage_intake/', HodViews.manage_intake, name="manage_intake"),
    path('edit_intake/<intake_id>/', HodViews.edit_intake, name="edit_intake"),
    path('edit_intake_save/', HodViews.edit_intake_save, name="edit_intake_save"),
    path('delete_intake/<intake_id>/', HodViews.delete_intake, name="delete_intake"),
    
    # Semester
    path('add_semester/', HodViews.add_semester, name="add_semester"),
    path('add_semester_save/', HodViews.add_semester_save, name="add_semester_save"),
    path('manage_semester/', HodViews.manage_semester, name="manage_semester"),
    path('edit_semester/<semester_id>/', HodViews.edit_semester, name="edit_semester"),
    path('edit_semester_save/', HodViews.edit_semester_save, name="edit_semester_save"),
    path('delete_semester/<semester_id>/', HodViews.delete_semester, name="delete_semester"),

    # admin student
    path('add_student/', HodViews.add_student, name="add_student"),
    path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    path('manage_student/', HodViews.manage_student, name="manage_student"),
    path('edit_student/<student_id>/', HodViews.edit_student, name="edit_student"),
    path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    # # admin Student
    # path('add_student/', HodViews.add_student, name="add_student"),
    # path('add_student_save/', HodViews.add_student_save, name="add_student_save"),
    # path('edit_student/<student_id>', HodViews.edit_student, name="edit_student"),
    # path('edit_student_save/', HodViews.edit_student_save, name="edit_student_save"),
    # path('manage_student/', HodViews.manage_student, name="manage_student"),
    # path('delete_student/<student_id>/', HodViews.delete_student, name="delete_student"),
    # admin subject
    path('add_subject/', HodViews.add_subject, name="add_subject"),
    path('add_subject_save/', HodViews.add_subject_save, name="add_subject_save"),
    path('manage_subject/', HodViews.manage_subject, name="manage_subject"),
    path('edit_subject/<subject_id>/', HodViews.edit_subject, name="edit_subject"),
    path('edit_subject_save/', HodViews.edit_subject_save, name="edit_subject_save"),
    path('delete_subject/<subject_id>/', HodViews.delete_subject, name="delete_subject"),
    #  admin more
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('admin_view_attendance/', HodViews.admin_view_attendance, name="admin_view_attendance"),
    path('admin_get_attendance_dates/', HodViews.admin_get_attendance_dates, name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', HodViews.admin_get_attendance_student, name="admin_get_attendance_student"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    


    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', StaffViews.get_students, name="get_students"),
    path('save_attendance_data/', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', StaffViews.update_attendance_data, name="update_attendance_data"),
    path('staff_profile/', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', StaffViews.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', StaffViews.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', StaffViews.staff_add_result_save, name="staff_add_result_save"),

    # URSL for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('course_registration/', StudentViews.course_registration, name="course_registration"),
    path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),    
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),
]
