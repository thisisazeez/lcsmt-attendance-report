from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
import datetime # To Parse input DateTime into Python Date Time Object
from django.shortcuts import render, get_object_or_404
from .forms import AssignmentAnwserForm, AssignmentForm,SolCreditForm
from .models import Assignment, Solution
from student_management_app.models import CustomUser,Docs, Departments, Semesters, Staffs, Courses, Subjects, Students, Attendance, Registrations # AttendanceReport,  StudentResult


def student_home(request):
    student_obj = Students.objects.get(admin=request.user.id)
    # student_id = student_obj.id
    # total_attendance = AttendanceReport.objects.filter(student_id=student_obj).count()
    # attendance_present = AttendanceReport.objects.filter(student_id=student_obj, status=True).count()
    # attendance_absent = AttendanceReport.objects.filter(student_id=student_obj, status=False).count()

    # course_obj = Courses.objects.get(id=student_obj.course_id.id)
    # total_subjects = Subjects.objects.filter(id=course_obj).count()

    subject_name = []
    data_present = []
    data_absent = []
    # subject_data = Subjects.objects.filter(id=student_obj.course_id)
    # for subject in subject_data:
    #     attendance = Attendance.objects.filter(subject_id=subject.id)
    #     attendance_present_count = Attendance.objects.filter(attendance_id__in=attendance, status=True, student_id=student_obj.id).count()
    #     attendance_absent_count = Attendance.objects.filter(attendance_id__in=attendance, status=False, student_id=student_obj.id).count()
    #     subject_name.append(subject.subject_name)
    #     data_present.append(attendance_present_count)
    #     data_absent.append(attendance_absent_count)
    
    context={
        # "total_attendance": total_attendance,
        # "attendance_present": attendance_present,
        # "attendance_absent": attendance_absent,
        # "total_subjects": total_subjects,
        "subject_name": subject_name,
        "data_present": data_present,
        "data_absent": data_absent
    }
    return render(request, "student_template/student_home_template.html", context)

def course_registration(request):
    student= Students.objects.get(admin = request.user.id)
    # for dept in departments:
    #     print( student.department)
    #     if student.department.id == dept.id:
    #         department = dept.id 
    #         break
    # student = Students.objects.get(admin = a)
    subjects = Subjects.objects.all()#(course= student.course.id)
    
    # print(subjects.course)
    # print(student.department.department_name)
    std_dept =student.department.department_name
    std_crs = student.course.course_name
    # for subject in subjects:
    #     if subject.course.course_name == std_crs:
    #         print (subject.subject_name)
    departments = Departments.objects.get(department_name=std_dept)
    # courses = Courses.objects.get(course_name= std_crs)
    # semesters = Semesters.objects.get(id=student.semester.id)
    # subjects = Subjects.objects.get(course= student.course.id)
    staffs = Staffs.objects.all()   
    # for sub in all_subjects:
    #     subjects = sub.objects.filter(course = course.id)
            
            
    
    context = {
        "std_dept":std_dept,
        "student":student,
        "subjects":subjects,
        "std_crs":std_crs
        # "semesters":semesters,
        # "courses":courses,
    }
    return render(request, "student_template/course_registration_template.html", context)

def course_registration_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('course_registration')
    else:
        student_id = request.POST.get('student_id')
        subject = request.POST.getlist('check_id')
        course = request.POST.get('course')
        semester = request.POST.get('semester')
        department = request.POST.get('department')

        print(subject)
        # try:
        course_reg = Registrations(subject=subject, student = Students.objects.get(id=student_id ))#Subjects.objects.get(id=subject))#semesters=Semesters.objects.get( semester_name=semester)) #Departments.objects.get( department_name=department), course=Courses.objects.get(course_name=course),
        course_reg.save()
        messages.success(request, "Subjects Registered Successfully!")
        return redirect('course_registration')
        # except:
        # messages.error(request, "Failed to Add student!")
        #     return redirect('course_registration')

def manage_course_registration(request):
    student= Students.objects.get(admin = request.user.id)

    subjects = Subjects.objects.all()#(course= student.course.id)
    
    # print(subjects.course)
    # print(student.department.department_name)
    std_dept =student.department.department_name
    std_crs = student.course.course_name
    # for subject in subjects:
    #     if subject.course.course_name == std_crs:
    #         print (subject.subject_name)
    departments = Departments.objects.get(department_name=std_dept)
    # courses = Courses.objects.get(course_name= std_crs)
    # semesters = Semesters.objects.get(id=student.semester.id)
    # subjects = Subjects.objects.get(course= student.course.id)
    # staffs = Staffs.objects.all()   
    # for sub in all_subjects:
    #     subjects = sub.objects.filter(course = course.id)
            
            
    
    context = {
        "departments":departments,
        "student":student,
        "subjects":subjects,
        "std_crs":std_crs,
        # "semesters":semesters,
        # "courses":courses,
    }
    return render(request, "student_template/manage_course_registration_template.html", context)
# def manage_course_registration(request):
#     student= Students.objects.get(admin = request.user.id)
#     registered_courses = Registrations.objects.get(student= student)
#     print(registered_courses.subject)
#     context = {
#         "registered_courses": registered_courses
#     }
#     return render(request, 'student_template/manage_course_registration_template.html', context)

# def manage_course_registration_save(request):
#     if request.method != "POST":
#         messages.error(request, "Invalid Method!")
#         return redirect('manage_course_registration')
#     else:
#         # subject = request.POST.get('subject')
#         subject = request.POST.get('subject')
#         # course = request.POST.get('course')
#         # semester = request.POST.get('semester')
#         # department = request.POST.get('department')

#         print(subject)
#         # try:
#         # course_reg = Registrations(subject=Subjects.objects.get(id=subject))#semesters=Semesters.objects.get( semester_name=semester)) #Departments.objects.get( department_name=department), course=Courses.objects.get(course_name=course),
#         # course_reg.save()
#         messages.success(request, "Subjects Registered Successfully!")
#         return redirect('manage_course_registration')
#         # except:
#         # messages.error(request, "Failed to Add student!")
#         #     return redirect('course_registration')

def edit_course_registration(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    courses = Courses.objects.all()
    departments = Departments.objects.all()
    semesters = Semesters.objects.all()
    course_registrations = Registrations.objects.all()
    context = {
        "subject": subject,
        "departments":departments,
        "course_registrations":course_registrations,
        "semesters":semesters,
        "courses":courses,
        "id": subject_id
    }
    return render(request, 'student_template/edit_course_registration_template.html', context)

def student_view_attendance(request):
    student = Students.objects.get(admin=request.user.id) # Getting Logged in Student Data
    course = student.course_id # Getting Course Enrolled of LoggedIn Student
    # course = Courses.objects.get(id=student.course_id.id) # Getting Course Enrolled of LoggedIn Student
    subjects = Subjects.objects.filter(course_id=course) # Getting the Subjects of Course Enrolled
    context = {
        "subjects": subjects
    }
    return render(request, "student_template/student_view_attendance.html", context)

def student_view_attendance_post(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('student_view_attendance')
    else:
        # Getting all the Input Data
        subject_id = request.POST.get('subject')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Parsing the date data into Python object
        start_date_parse = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_parse = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        # Getting all the Subject Data based on Selected Subject
        subject_obj = Subjects.objects.get(id=subject_id)
        # Getting Logged In User Data
        user_obj = CustomUser.objects.get(id=request.user.id)
        # Getting Student Data Based on Logged in Data
        stud_obj = Students.objects.get(admin=user_obj)

        # Now Accessing Attendance Data based on the Range of Date Selected and Subject Selected
        attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse, end_date_parse), subject_id=subject_obj)
        # Getting Attendance Report based on the attendance details obtained above
        attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=stud_obj)

        # for attendance_report in attendance_reports:
        #     print("Date: "+ str(attendance_report.attendance_id.attendance_date), "Status: "+ str(attendance_report.status))

        # messages.success(request, "Attendacne View Success")

        context = {
            "subject_obj": subject_obj,
            "attendance_reports": attendance_reports
        }

        return render(request, 'student_template/student_attendance_data.html', context)

def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)

    context={
        "user": user,
        "student": student
    }
    return render(request, 'student_template/student_profile.html', context)

def student_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('student_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            student = Students.objects.get(admin=customuser.id)
            student.address = address
            student.save()
            
            messages.success(request, "Profile Updated Successfully")
            return redirect('student_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('student_profile')

def student_view_result(request):
    student = Students.objects.get(admin=request.user.id)
    student_result = StudentResult.objects.filter(id=student.id)
    context = {
        "student_result": student_result,
    }
    return render(request, "student_template/student_view_result.html", context)

def submit(request):#, assignment_id
    
    if request.method == 'POST':
        form = AssignmentAnwserForm(request.POST, request.FILES)
        print ("it dosnt work from here")
        if form.is_valid():
            print ("it works from here too")
            newAns = Solution(answer = request.FILES['anwser'])
            newAns.save()
            print("It is ok here too")

            return HttpResponseRedirect('/submit')
    else:
        # assignment=Assignment.objects.all() #get(id=assignment_id)
        # if request.method == 'POST':
        #     # print(request.POST['title'])
        form = AssignmentAnwserForm()#user=request.user,course=assignment.course, data=request.POST
        #     if form.is_valid():
        #         solution = form.save(commit=False)
        #         solution.student = Students.objects.get(user=request.user)
        #         solution.assignment=assignment
        #         pre_sol=Solution.objects.all() #filter(assignment__id=assignment_id,student=solution.student).
        #         pre_sol.delete()
        #         solution.save()
        #         return redirect('student_home',course=assignment.course)
        #     else:
        # form = AssignmentAnwserForm()#user=request.user,course=assignment.course
        return render(request, 'student_template/sol_submit.html', {'form': form})#user=request.user
            
            
def detail(request):#, assign_id
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'error_message': "You must be logged in!!"})
    else:
        user = request.user
        assign = Docs.objects.all()#, pk=assign_id get_object_or_404
        return render(request, 'student_template/details.html', {'assignments': assign, 'user': user,})#'course':assign.course.name

        

def add_t(request):
    course = Courses.objects.all()

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        print ("it dosnt work from here")
        if form.is_valid():
            print ("it works from here too")
            newAssi = Docs(docfile = request.FILES['docfile'])
            newAssi.save()
            # course=Courses.objects.get(course_name=course)
            # print(course)
            # ass.teacher = CustomUser.objects.get(user=request.user, user_type=2)
            # ass.course=course
        # ass.save()
        return HttpResponseRedirect('/staff_home')
    else:
        # print("###########")
        form = AssignmentForm()
    
    docs = Docs.objects.all()
    return render(request, 'staff_template/add_t.html', {'form': form, 'docs':docs})