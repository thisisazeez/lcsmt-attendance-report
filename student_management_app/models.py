
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    apple= "apple"
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Sessions(models.Model):
    id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Intakes(models.Model):
    id = models.AutoField(primary_key=True)
    intake_name = models.CharField(max_length=255)
    session = models.ForeignKey(Sessions,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Semesters(models.Model):
    id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    department_name = models.ForeignKey(Departments,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    # def __str__(self):
	#     return self.course_name

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    # intake = models.ForeignKey(Intakes,on_delete=models.CASCADE)
    semesters= models.ForeignKey(Semesters,on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True, null=True) #need to give default course
    staff = models.ForeignKey(Staffs, on_delete=models.CASCADE, blank=True, null=True)
    # registered_student = models.ForeignKey(Students, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class AssignLecturer(models.Model):
    id = models.AutoField(primary_key=True)
    assign_course= models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True) #need to give default course
    assign_staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    assign_department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    assign_intake = models.ForeignKey(Intakes, on_delete=models.CASCADE, null=True, blank=True)
    assign_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True, blank=True)
    assign_semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, null=True, blank=True)
    objects = models.Manager()

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    intake = models.ForeignKey(Intakes, on_delete=models.DO_NOTHING, default=1)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, blank=True, null=True)
    # session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    # registered_subjects = models.ForeignKey(Registrations, on_delete=models.DO_NOTHING)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Registretions(models.Model):
    id = models.AutoField(primary_key=True)
    registretion_name = models.CharField(max_length=255)
    student = models.ForeignKey(Students, on_delete=models.DO_NOTHING, blank=True, null=True)
    session = models.ForeignKey(Sessions, on_delete=models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING, blank=True, null=True)
    # subject_choice = models.Choices()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING, blank=True, null=True)
    attendance_date = models.DateField(auto_now=True)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE, blank=True, null=True)
    students = models.ForeignKey(Students, on_delete=models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey(Staffs, on_delete=models.DO_NOTHING, blank=True, null=True)
    present = models.BooleanField(blank=True, null=True)
    assignment = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


# class AttendanceReport(models.Model):
    # Individual Student Attendance
    # id = models.AutoField(primary_key=True)
    # student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    # attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    # status = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # objects = models.Manager()




# class StudentResult(models.Model):
    # id = models.AutoField(primary_key=True)
    # student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    # subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    # subject_exam_marks = models.FloatField(default=0)
    # subject_assignment_marks = models.FloatField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # objects = models.Manager()


#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(admin=instance, course_id=Courses.objects.get(id=1), session_year_id=SessionYearModel.objects.get(id=1), address="", profile_pic="", gender="")
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()