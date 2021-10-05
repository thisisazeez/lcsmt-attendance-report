from django import forms 
from django.forms import Form
from .models import Assignment, Solution, Students






class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['title','answer']

	# def __init__(self, *args, **kwargs):
        
	# 	user = kwargs.pop('user')
	# 	usr_year = Students.objects.get(user=user).id
	# 	course=kwargs.pop('course')
		# print("##############" + str(usr_year))
		# usr_assign = Assignment.objects.filter(year=usr_year)
		# super(SolutionForm, self).__init__(*args, **kwargs)
		#self.fields['assignment'].queryset = Assignment.objects.filter(year=usr_year,course__name=course)


class AssignmentForm(Form):
	
    docfile = forms.FileField(
		label='select a file',
		help_text='max. 42 megabytes'
	)
	# class Meta:
	# 	model=Assignment
	# 	fields=['num','name','questions','deadline']

class SolCreditForm(forms.ModelForm):
	class Meta:
		model=Solution
		fields=['points','comments']




# class DateInput(forms.DateInput):
#     input_type = "date"



# class AddStudentForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
#     password = forms.CharField(label="Password", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "value":"lincoln1234567890"}), )
#     first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))#disabled=True
#     username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     student_id = forms.CharField(label="Student ID", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     #For Displaying Courses
#     try:
#         courses = Courses.objects.all()
#         course_list = []
#         for course in courses:
#             single_course = (course.id, course.course_name)
#             course_list.append(single_course)
#     except:
#         course_list = []
    
#     #For Displaying Session Years
#     try:
#         session_years = SessionYearModel.objects.all()
#         session_year_list = []
#         for session_year in session_years:
#             single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
#             session_year_list.append(single_session_year)
            
#     except:
#         session_year_list = []
    
#     gender_list = (
#         ('Male','Male'),
#         ('Female','Female')
#     )
    
#     course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
#     gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
#     session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
#     # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
#     # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
#     profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))



# class EditStudentForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
#     first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
#     address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

#     #For Displaying Courses
#     try:
#         courses = Courses.objects.all()
#         course_list = []
#         for course in courses:
#             single_course = (course.id, course.course_name)
#             course_list.append(single_course)
#     except:
#         course_list = []

#     #For Displaying Session Years
#     try:
#         session_years = SessionYearModel.objects.all()
#         session_year_list = []
#         for session_year in session_years:
#             single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
#             session_year_list.append(single_session_year)
            
#     except:
#         session_year_list = []

    
#     gender_list = (
#         ('Male','Male'),
#         ('Female','Female')
#     )
    
#     course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
#     gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
#     session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
#     # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
#     # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
#     profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))