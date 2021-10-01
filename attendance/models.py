from django.db import models
# import misaka
from student_management_app.models import Students, Staffs


class MessageToTeacher(models.Model):
    student = models.ForeignKey(Students,related_name='student',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staffs,related_name='messages',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    # def save(self,*args,**kwargs):
    #     self.message_html = misaka.html(self.message)
    #     super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['student','message']

class ClassNotice(models.Model):
    teacher = models.ForeignKey(Staffs,related_name='teacher',on_delete=models.CASCADE)
    students = models.ManyToManyField(Students,related_name='class_notice')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.message

    # def save(self,*args,**kwargs):
    #     self.message_html = misaka.html(self.message)
    #     super().save(*args,**kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['teacher','message']

class ClassAssignment(models.Model):
    student = models.ManyToManyField(Students,related_name='student_assignment')
    teacher = models.ForeignKey(Staffs,related_name='teacher_assignment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    assignment_name = models.CharField(max_length=250)
    assignment = models.FileField(upload_to='assignments')

    def __str__(self):
        return self.assignment_name

    class Meta:
        ordering = ['-created_at']

class SubmitAssignment(models.Model):
    student = models.ForeignKey(Students,related_name='student_submit',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staffs,related_name='teacher_submit',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    submitted_assignment = models.ForeignKey(ClassAssignment,related_name='submission_for_assignment',on_delete=models.CASCADE)
    submit = models.FileField(upload_to='Submission')

    def __str__(self):
        return "Submitted"+str(self.submitted_assignment.assignment_name)

    class Meta:
        ordering = ['-created_at']
