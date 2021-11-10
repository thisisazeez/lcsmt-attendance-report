from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.template import RequestContext
# from django.core.urlresolvers import reverse 
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.shortcuts import render, get_object_or_404
from .forms import SolutionForm, AssignmentForm,SolCreditForm
from .models import Assignment, Solution
from django.urls import reverse
from .forms import AssignmentForm
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


from student_management_app.models import CustomUser, Docs, Departments, Intakes, Staffs, Courses, Subjects, Students, SessionYearModel, Attendance, AttendanceReport #StudentResult


def staff_home(request):
    # Fetching All Students under Staff

    subjects = Subjects.objects.filter(id=request.user.id)
    course_id_list = []
    # for subject in subjects:
    #     course = Courses.objects.get(id=subject.course_id.id)
    #     course_id_list.append(course.id)
    
    final_course = []
    # Removing Duplicate Course Id
    for course_id in course_id_list:
        if course_id not in final_course:
            final_course.append(course_id)
    
    # students_count = Students.objects.filter(course_id__in=final_course).count()
    subject_count = subjects.count()

    # Fetch All Attendance Count
    attendance_count = Attendance.objects.filter(subject_id__in=subjects).count()

    #Fetch Attendance Data by Subjects
    subject_list = []
    attendance_list = []
    # for subject in subjects:
    #     attendance_count1 = Attendance.objects.filter(subject_id=subject.id).count()
    #     subject_list.append(subject.subject_name)
    #     attendance_list.append(attendance_count1)

    # students_attendance = Students.objects.filter(course_id__in=final_course)
    student_list = []
    student_list_attendance_present = []
    student_list_attendance_absent = []
    # for student in students_attendance:
    #     attendance_present_count = AttendanceReport.objects.filter(status=True, student_id=student.id).count()
    #     attendance_absent_count = AttendanceReport.objects.filter(status=False, student_id=student.id).count()
    #     student_list.append(student.admin.first_name+" "+ student.admin.last_name)
    #     student_list_attendance_present.append(attendance_present_count)
    #     student_list_attendance_absent.append(attendance_absent_count)

    context={
        # "students_count": students_count,
        # "attendance_count": attendance_count,
        # "subject_count": subject_count,
        # "subject_list": subject_list,
        # "attendance_list": attendance_list,
        "student_list": student_list,
        "attendance_present_list": student_list_attendance_present,
        "attendance_absent_list": student_list_attendance_absent
    }
    return render(request, "staff_template/staff_home_template.html", context)

 

def staff_take_attendance(request):
    departments = Departments.objects.filter()
    intakes = Intakes.objects.all()
    subjects = Subjects.objects.all()
    context = {
        "departments": departments,
        "intakes": intakes,
        "subjects":subjects,
    }
    return render(request, "staff_template/take_attendance_template.html", context)



# WE don't need csrf_token when using Ajax
@csrf_exempt
def get_students(request):
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
    # Students enroll to Course, Course has Subjects
    # Getting all data from subject model based on subject_id
    # subject_model = Subjects.objects.get(id=subject_id)

    # session_model = SessionYearModel.objects.get(id=session_year)

    # students = Students.objects.filter(id=subject_model.course_id, session_year_id=session_model)

    # # Only Passing Student Id and Student Name Only
    # list_data = []

    # for student in students:
    #     data_small={"id":student.admin.id, "name":student.admin.first_name+" "+student.admin.last_name}
    #     list_data.append(data_small)
    
    return render(request, "staff_template/get_students.html", context)

    # return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

def submit_attendance(request):
    # print(json.loads(request.POST['body']))
    if request.method == 'POST':
        department_id = int(request.POST.get('department'))
        intake_id = int(request.POST.get('intake'))
        subject_id = int(request.POST.get('subject'))
        department = Departments.objects.get(id=department_id)
        intake = Intakes.objects.get(id=intake_id)
        subject = Subjects.objects.get(id=subject_id)
        for key, value in request.POST.items():
            if key == 'csrfmiddlewaretoken' or key == 'department' or key == 'intake' or key == 'subject':
                pass
            else:
                attendance = Attendance.objects.create (
                    department = department,
                    intake = intake,
                    subject = subject,
                    students = Students.objects.get(id = int(key)),
                    # staff = request.user,
                    present = True,
                    absent = True,
                    medic_leave = True,
                    assignment = True
                )
                attendance.save()
        return HttpResponse('<h1>Attendance taken</h1>')


@csrf_exempt
def save_attendance_data(request):
    # Get Values from Staf Take Attendance form via AJAX (JavaScript)
    # Use getlist to access HTML Array/List Input Data
    student_ids = request.POST.get("student_ids")
    subject_id = request.POST.get("subject_id")
    attendance_date = request.POST.get("attendance_date")
    session_year_id = request.POST.get("session_year_id")

    subject_model = Subjects.objects.get(id=subject_id)
    session_year_model = SessionYearModel.objects.get(id=session_year_id)

    json_student = json.loads(student_ids)
    # print(dict_student[0]['id'])

    # print(student_ids)
    try:
        # First Attendance Data is Saved on Attendance Model
        attendance = Attendance(subject_id=subject_model, attendance_date=attendance_date, session_year_id=session_year_model)
        attendance.save()

        for stud in json_student:
            # Attendance of Individual Student saved on AttendanceReport Model
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")




def staff_update_attendance(request):
    subjects = Subjects.objects.filter(id=request.user.id)
    session_years = SessionYearModel.objects.all()
    context = {
        "subjects": subjects,
        "session_years": session_years
    }
    return render(request, "staff_template/update_attendance_template.html", context)

@csrf_exempt
def get_attendance_dates(request):
    

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
def get_attendance_student(request):
    # Getting Values from Ajax POST 'Fetch Student'
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id, "name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name, "status":student.status}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def update_attendance_data(request):
    student_ids = request.POST.get("student_ids")

    attendance_date = request.POST.get("attendance_date")
    attendance = Attendance.objects.get(id=attendance_date)

    json_student = json.loads(student_ids)

    try:
        
        for stud in json_student:
            # Attendance of Individual Student saved on AttendanceReport Model
            student = Students.objects.get(admin=stud['id'])

            attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance)
            attendance_report.status=stud['status']

            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")


def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)

    context={
        "user": user,
        "staff": staff
    }
    return render(request, 'staff_template/staff_profile.html', context)


def staff_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('staff_profile')
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

            staff = Staffs.objects.get(admin=customuser.id)
            staff.address = address
            staff.save()

            messages.success(request, "Profile Updated Successfully")
            return redirect('staff_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('staff_profile')



def staff_add_result(request):
    subjects = Subjects.objects.filter(id=request.user.id)
    session_years = SessionYearModel.objects.all()
    context = {
        "subjects": subjects,
        "session_years": session_years,
    }
    return render(request, "staff_template/add_result_template.html", context)


def staff_add_result_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('staff_add_result')
    else:
        student_admin_id = request.POST.get('student_list')
        assignment_marks = request.POST.get('assignment_marks')
        exam_marks = request.POST.get('exam_marks')
        subject_id = request.POST.get('subject')

        student_obj = Students.objects.get(admin=student_admin_id)
        subject_obj = Subjects.objects.get(id=subject_id)

        try:
            # Check if Students Result Already Exists or not
            check_exist = StudentResult.objects.filter(subject_id=subject_obj, student_id=student_obj).exists()
            if check_exist:
                result = StudentResult.objects.get(subject_id=subject_obj, student_id=student_obj)
                result.subject_assignment_marks = assignment_marks
                result.subject_exam_marks = exam_marks
                result.save()
                messages.success(request, "Result Updated Successfully!")
                return redirect('staff_add_result')
            else:
                result = StudentResult(student_id=student_obj, subject_id=subject_obj, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
                result.save()
                messages.success(request, "Result Added Successfully!")
                return redirect('staff_add_result')
        except:
            messages.error(request, "Failed to Add Result!")
            return redirect('staff_add_result')
        
        
def add_t(request):
    course = Courses.objects.all()

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        name  =  request.POST.get("name")
        print ("it dosnt work from here")
        if form.is_valid():
            print ("it works from here too")
            newAssi = Docs(docfile = request.FILES['docfile'], doc_name=name )
            
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
    return render(request, 'staff_template/add_t.html', {'form': form, 'docs':docs})# context_instance=RequestContext(request))#, course=course
            
def detail_t(request):#, assign_id
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'error_message': "You must be logged in!!"})
    else:
        user = request.user
        assign =(Assignment)#, pk=assign_id  get_object_or_404
        sol_set=Solution.objects.all() #filter(assignment__id=assign_id)
        return render(request, 'staff_template/details_t.html', {'assignment': assign,'sol_set':sol_set, 'user': user})#,'course':assign.course.name

def sol_detail_t(request): #sol_id
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'error_message': "You must be logged in!!"})
    else:
        ass = Solution.objects.all()
        sol= (Solution.objects.all())
        # if request.method=='POST':
        #     stt=request.POST['comments']
        #     sol.comments=stt
        #     sol.points=request.POST['points']
        #     sol.save()
        #     return redirect('staff_home', course=sol.assignment.course), 'sol':sol,
        return render(request,'staff_template/sol_details_t.html',{'ass':ass})

