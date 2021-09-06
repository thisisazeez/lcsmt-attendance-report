from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, Departments 
# from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, NotificationStudent, NotificationStaffs,
# >>>>>>> bf60ba236680392d8e2fc6997476aa5f15209cf9

# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)

admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
# <<<<<<< HEAD
# admin.site.register(NotificationStudent)
# admin.site.register(NotificationStaffs)
# =======
# admin.site.register(NotificationStudent)
# admin.site.register(NotificationStaffs)
admin.site.register(Departments)
# >>>>>>> bf60ba236680392d8e2fc6997476aa5f15209cf9
