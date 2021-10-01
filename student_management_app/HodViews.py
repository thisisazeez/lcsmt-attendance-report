from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from student_management_app.models import CustomUser, Staffs, Departments, Courses, Subjects, Students, Intakes, Semesters, SessionYearModel, Attendance # AttendanceReport
# from .forms import AddStudentForm, EditStudentForm


def admin_home(request):
    all_student_count = Students.objects.all().count()
    subject_count = Subjects.objects.all().count()
    course_count = Courses.objects.all().count()
    staff_count = Staffs.objects.all().count()

    # Total Subjects and students in Each Course
    course_all = Courses.objects.all()
    course_name_list = []
    subject_count_list = []
    student_count_list_in_course = []

    for course in course_all:
        subjects = Subjects.objects.filter(id=course.id).count()
        students = Students.objects.filter(id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
        student_count_list_in_course.append(students)
    
    subject_all = Subjects.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    for subject in subject_all:
        course = Courses.objects.all()
        student_count = Students.objects.all().count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count)
    
    # For Saffs
    staff_attendance_present_list=[]
    staff_attendance_leave_list=[]
    staff_name_list=[]

    staffs = Staffs.objects.all()
    for staff in staffs:
        subject_ids = Subjects.objects.filter(id=staff.admin.id)
        attendance = Attendance.objects.filter(subject_id__in=subject_ids).count()
        staff_attendance_present_list.append(attendance)
        staff_name_list.append(staff.admin.first_name)

    # For Students
    student_attendance_present_list=[]
    student_attendance_leave_list=[]
    student_name_list=[]

    students = Students.objects.all()
    for student in students:
        # attendance = Attendance.objects.filter(student_id=student.id, status=True).count()
        # absent = Attendance.objects.filter(student_id=student.id, status=False).count()
        # student_attendance_present_list.append(attendance)
        student_name_list.append(student.admin.first_name)


    context={
        "all_student_count": all_student_count,
        "subject_count": subject_count,
        "course_count": course_count,
        "staff_count": staff_count,
        "course_name_list": course_name_list,
        "subject_count_list": subject_count_list,
        "student_count_list_in_course": student_count_list_in_course,
        "subject_list": subject_list,
        "student_count_list_in_subject": student_count_list_in_subject,
        "staff_attendance_present_list": staff_attendance_present_list,
        "staff_attendance_leave_list": staff_attendance_leave_list,
        "staff_name_list": staff_name_list,
        "student_attendance_present_list": student_attendance_present_list,
        "student_attendance_leave_list": student_attendance_leave_list,
        "student_name_list": student_name_list,
    }
    return render(request, "hod_template/home_content.html", context)

# #staff
def add_staff(request):
    return render(request, "hod_template/add_staff_template.html")

def add_staff_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = "lincolnstaff12345"
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
            user.staffs.address = address
            user.save()
            messages.success(request, "Staff Added Successfully!")
            return redirect('add_staff')
        except:
            messages.error(request, "Failed to Add Staff!")
            return redirect('add_staff')

def manage_staff(request):
    staffs = Staffs.objects.all()
    context = {
        "staffs": staffs
    }
    return render(request, "hod_template/manage_staff_template.html", context)

def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff": staff,
        "id": staff_id
    }
    return render(request, "hod_template/edit_staff_template.html", context)

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get('staff_id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            if password != None and password != "":
                user.set_password(password)
            user.username = username
            user.save()
            
            # INSERTING into Staff Model
            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, "Staff Updated Successfully.")
            return redirect('/edit_staff/'+staff_id)

        except:
            messages.error(request, "Failed to Update Staff.")
            return redirect('/edit_staff/'+staff_id)

def delete_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully.")
        return redirect('manage_staff')
    except:
        messages.error(request, "Failed to Delete Staff.")
        return redirect('manage_staff')


# #semester
def add_semester(request):
    return render(request, "hod_template/add_semester_template.html")

def add_semester_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_semester')
    else:
        semester = request.POST.get('semester')
        try:
            semester_model = Semesters(semester_name=semester)
            semester_model.save()
            messages.success(request, "Semester Added Successfully!")
            return redirect('add_semester')
        except:
            messages.error(request, "Failed to Add Semester!")
            return redirect('add_semester')
        
def manage_semester(request):
    semesters = Semesters.objects.all()
    context = {
        "semesters": semesters
    }
    return render(request, 'hod_template/manage_semester_template.html', context)

def edit_semester(request, semester_id):
    semester = Semesters.objects.get(id=semester_id)
    context = {
        "semester": semester,
        "id": semester_id
    }
    return render(request, 'hod_template/edit_semester_template.html', context)

def edit_semester_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        semester_id = request.POST.get('semester_id')
        semester_name = request.POST.get('semester')

        try:
            semester = Semesters.objects.get(id=semester_id)
            semester.semester_name = semester_name
            semester.save()

            messages.success(request, "semester Updated Successfully.")
            return redirect('/edit_semester/'+semester_id)

        except:
            messages.error(request, "Failed to Update semester.")
            return redirect('/edit_semester/'+semester_id)

def delete_semester(request, semester_id):
    semester = Semesters.objects.get(id=semester_id)
    try:
        semester.delete()
        messages.success(request, "Semester Deleted Successfully.")
        return redirect('manage_semester')
    except:
        messages.error(request, "Failed to Delete Semester.")
        return redirect('manage_semester')

# #department
def add_department(request):
    return render(request, "hod_template/add_department_template.html")

def add_department_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_department')
    else:
        department = request.POST.get('department')
        try:
            department_model = Departments(department_name=department)
            department_model.save()
            messages.success(request, "Department Added Successfully!")
            return redirect('add_department')
        except:
            messages.error(request, "Failed to Add Department!")
            return redirect('add_department')

def manage_department(request):
    departments = Departments.objects.all()
    context = {
        "departments": departments
    }
    return render(request, 'hod_template/manage_department_template.html', context)

def edit_department(request, department_id):
    department = Departments.objects.get(id=department_id)
    context = {
        "department": department,
        "id": department_id
    }
    return render(request, 'hod_template/edit_department_template.html', context)

def edit_department_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department')

        try:
            department = Departments.objects.get(id=department_id)
            department.department_name = department_name
            department.save()

            messages.success(request, "department Updated Successfully.")
            return redirect('/edit_department/'+department_id)

        except:
            messages.error(request, "Failed to Update department.")
            return redirect('/edit_department/'+department_id)

def delete_department(request, department_id):
    department = Departments.objects.get(id=department_id)
    try:
        department.delete()
        messages.success(request, "department Deleted Successfully.")
        return redirect('manage_department')
    except:
        messages.error(request, "Failed to Delete department.")
        return redirect('manage_department')

#  #course
def add_course(request):
    departments = Departments.objects.all()
    context = {
        "departments":departments,
    }
    return render(request, "hod_template/add_course_template.html", context)

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        course = request.POST.get('course')
        choices = request.POST.get('department')
        # department = Departments.objects.filter()
        # try:
        course_model = Courses(course_name=course, department_name=Departments.objects.get(id=choices))
        course_model.save()
        messages.success(request, "Course Added Successfully!")
        return redirect('add_course')
        # except:
        #     messages.error(request, "Failed to Add Course!")
        #     return redirect('add_course')

def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'hod_template/manage_course_template.html', context)

def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        "course": course,
        "id": course_id
    }
    return render(request, 'hod_template/edit_course_template.html', context)

def edit_course_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()

            messages.success(request, "Course Updated Successfully.")
            return redirect('/edit_course/'+course_id)

        except:
            messages.error(request, "Failed to Update Course.")
            return redirect('/edit_course/'+course_id)

def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully.")
        return redirect('manage_course')
    except:
        messages.error(request, "Failed to Delete Course.")
        return redirect('manage_course')

# #intake
def add_intake(request):
    return render(request, "hod_template/add_intake_template.html")

def add_intake_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_intake')
    else:
        intake = request.POST.get('intake')
        try:
            intake_model = Intakes(intake_name=intake)
            intake_model.save()
            messages.success(request, "intake Added Successfully!")
            return redirect('add_intake')
        except:
            messages.error(request, "Failed to Add intake!")
            return redirect('add_intake')

def manage_intake(request):
    intakes = Intakes.objects.all()
    context = {
        "intakes": intakes
    }
    return render(request, 'hod_template/manage_intake_template.html', context)

def edit_intake(request, intake_id):
    intake = Intakes.objects.get(id=intake_id)
    context = {
        "intake": intake,
        "id": intake_id
    }
    return render(request, 'hod_template/edit_intake_template.html', context)

def edit_intake_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method")
    else:
        intake_id = request.POST.get('intake_id')
        intake_name = request.POST.get('intake')

        try:
            intake = Intakes.objects.get(id=intake_id)
            intake.intake_name = intake_name
            intake.save()

            messages.success(request, "intake Updated Successfully.")
            return redirect('/edit_intake/'+intake_id)

        except:
            messages.error(request, "Failed to Update intake.")
            return redirect('/edit_intake/'+intake_id)

def delete_intake(request, intake_id):
    intake = Intakes.objects.get(id=intake_id)
    try:
        intake.delete()
        messages.success(request, "intake Deleted Successfully.")
        return redirect('manage_intake')
    except:
        messages.error(request, "Failed to Delete intake.")
        return redirect('manage_intake')

# #session
def manage_session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        "session_years": session_years
    }
    return render(request, "hod_template/manage_session_template.html", context)

def add_session(request):
    return render(request, "hod_template/add_session_template.html")

def add_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_course')
    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
            sessionyear.save()
            messages.success(request, "Session Year added Successfully!")
            return redirect("add_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect("add_session")

def edit_session(request, session_id):
    session_year = SessionYearModel.objects.get(id=session_id)
    context = {
        "session_year": session_year
    }
    return render(request, "hod_template/edit_session_template.html", context)

def edit_session_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('manage_session')
    else:
        session_id = request.POST.get('session_id')
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            session_year = SessionYearModel.objects.get(id=session_id)
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()

            messages.success(request, "Session Year Updated Successfully.")
            return redirect('/edit_session/'+session_id)
        except:
            messages.error(request, "Failed to Update Session Year.")
            return redirect('/edit_session/'+session_id)

def delete_session(request, session_id):
    session = SessionYearModel.objects.get(id=session_id)
    try:
        session.delete()
        messages.success(request, "Session Deleted Successfully.")
        return redirect('manage_session')
    except:
        messages.error(request, "Failed to Delete Session.")
        return redirect('manage_session')

# #students

def add_student(request):
    # departments = Departments.objects.all()
    # courses = Courses.objects.all()
    # intakes = Intakes.objects.all()
    # # sessions = SessionYearModel.objects.all()
    # context = {
    #     "departments":departments,
    #     "courses":courses,
    #     "intakes":intakes,
        # "sessions":sessions,
    # }
    return render(request, 'hod_template/add_student_template.html')

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_student')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = "lincolnstudent12345"
        parent_password = "password"
        address = request.POST.get('address')

        # course = request.POST.get('course')
        # department = request.POST.get('department')
        # intake = request.POST.get('intake')
        # gender = request.POST.get('gender')
        # session = request.POST.get('session')

        # try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, 
        last_name=last_name, first_name=first_name, parent_password=parent_password, user_type=3)
        user.students.address = address
        user.save()
        messages.success(request, "student Added Successfully!")
        return redirect('add_student')
        # except:
        #     messages.error(request, "Failed to Add student!")
        #     return redirect('add_student')

def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    return render(request, "hod_template/manage_student_template.html", context)

def edit_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    departments = Departments.objects.all()
    courses = Courses.objects.all()
    intakes = Intakes.objects.all()
    # sessions = SessionYearModel.objects.all()
    context = {
        # "sessions":sessions
        "departments":departments,
        "courses":courses,
        "intakes":intakes,
        "student": student,
        "student_id": student_id
    }
    return render(request, "hod_template/edit_student_template.html", context)

def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        course = request.POST.get('course')
        department = request.POST.get('department')
        intake = request.POST.get('intake')
        gender = request.POST.get('gender')
        session = request.POST.get('session')
        password = request.POST.get('password')


        # try:
        # INSERTING into Customuser Model
        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        if password != None and password != "":
            user.set_password(password)
        user.username = username
        user.save()
        
        # INSERTING into student Model
        print(department)
        student_model = Students.objects.get(admin=student_id)
        student_model.department=Departments.objects.get(id=department) 
        # session=SessionYearModel.objects.get( session_name=session), 
        student_model.intake=Intakes.objects.get(intake_name=intake)
        student_model.course=Courses.objects.get(course_name=course)
        student_model.gender=gender
        student_model.address = address
        student_model.save()

        messages.success(request, "student Updated Successfully.")
        return redirect('/edit_student/'+student_id)

        # except:
        #     messages.error(request, "Failed to Update student.")
        #     return redirect('/edit_student/'+student_id)
def delete_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request, "student Deleted Successfully.")
        return redirect('manage_student')
    except:
        messages.error(request, "Failed to Delete student.")
        return redirect('manage_student')


# #subject
def add_subject(request):
    departments = Departments.objects.all()
    staffs = Staffs.objects.all()
    courses = Courses.objects.all()
    semesters = Semesters.objects.all()

    context = {
        "departments":departments,
        "staffs":staffs,
        "semesters":semesters,
        "courses":courses,

    }
    return render(request, "hod_template/add_subject_template.html", context)

def add_subject_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_subject')
    else:
        subject = request.POST.get('subject')
        staff = request.POST.get('staff')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        department = request.POST.get('department')

        print(department)
        # try:
        subject_model = Subjects(subject_name=subject, department=Departments.objects.get(id=department), semesters=Semesters.objects.get( semester_name=semester), course=Courses.objects.get(course_name=course), staff=Staffs.objects.get(id=staff))
        subject_model.save  ()
        messages.success(request, "subject Added Successfully!")
        return redirect('add_subject')
        # except:
        #     messages.error(request, "Failed to Add subject!")
        #     return redirect('add_subject')

def manage_subject(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'hod_template/manage_subject_template.html', context)

def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    departments = Departments.objects.all()
    semesters = Semesters.objects.all()
    staffs = Staffs.objects.all()
    context = {
        "subject": subject,
        "departments":departments,
        "staffs":staffs,
        "semesters":semesters,
        "courses":courses,
        "id": subject_id
    }
    return render(request, 'hod_template/edit_subject_template.html', context)

def edit_subject_save(request):
    if request.method != "POST":
        HttpResponse("Invalid Method.")
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject')
        staff = request.POST.get('staff')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        department = request.POST.get('department')


        # print(subject_id)
        # try:
        subject = Subjects.objects.get(id=subject_id)
        subject.subject_name = subject_name

        course = Courses.objects.get(course_name=course)
        subject.course = course

        semester_name = Semesters.objects.get(semester_name=semester)
        subject.semesters = semester_name

        department_name = Departments.objects.get(department_name=department)
        subject.department = department_name

        staff_id = Staffs.objects.get(id=staff)
        subject.staff = staff_id
        
        subject.save()

        messages.success(request, "Subject Updated Successfully.")
        return redirect('/edit_subject/'+subject_id)
        # return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))

            # except:
            #     messages.error(request, "Failed to Update Subject.")
            #     # return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id}))
            #     return redirect('/edit_subject/'+subject_id)

def delete_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    try:
        subject.delete()
        messages.success(request, "Subject Deleted Successfully.")
        return redirect('manage_subject')
    except:
        messages.error(request, "Failed to Delete Subject.")
        return redirect('manage_subject')


def get_attendance(request):
    # Getting Values from Ajax POST 'Fetch Student'
    department_id = request.POST.get("department")
    intake_id = request.POST.get("intake")
    subject_id = request.POST.get("subject")

    print(subject_id)
    department = Departments.objects.get(id = department_id)
    intake = Intakes.objects.get(id = intake_id)
    subject = Subjects.objects.get(id = subject_id)
    students = Students.objects.filter(department=department).filter(intake=intake)# .filter(subject=subject)
    
    context = {
        'department': department,
        'intake': intake,
        'students': students,
        'subject' : subject,
    }

    return render(request, "hod_template/get_attendace.html", context)


# The exempts

@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def admin_view_attendance(request):
    subjects = Subjects.objects.all()
    session_years = SessionYearModel.objects.all()
    context = {
        "subjects": subjects,
        "session_years": session_years
    }
    return render(request, "hod_template/admin_view_attendance.html", context)

@csrf_exempt
def admin_get_attendance_dates(request):
    # Getting Values from Ajax POST 'Fetch Student'
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year_id")

    # Students enroll to Course, Course has Subjects
    # Getting all data from subject model based on subject_id
    subject_model = Subjects.objects.get(id=subject_id)

    session_model = SessionYearModel.objects.get(id=session_year)

    # students = Students.objects.filter(course_id=subject_model.course_id, session_year_id=session_model)
    attendance = Attendance.objects.filter(subject_id=subject_model, session_year_id=session_model)

    # Only Passing Student Id and Student Name Only
    list_data = []

    for attendance_single in attendance:
        data_small={"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "session_year_id":attendance_single.session_year_id.id}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def admin_get_attendance_student(request):
    # Getting Values from Ajax POST 'Fetch Student'
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = Attendance.objects.filter(attendance_id=attendance)
    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id, "name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name, "status":student.status}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'hod_template/admin_profile.html', context)

def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
    
def staff_profile(request):
    pass

def student_profile(requtest):
    pass




