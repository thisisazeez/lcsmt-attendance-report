from django.contrib import admin
from .models import ClassAssignment, ClassNotice, MessageToTeacher, SubmitAssignment
# Register your models here.

admin.site.register(ClassNotice)
admin.site.register(MessageToTeacher)
admin.site.register(SubmitAssignment)
admin.site.register(ClassAssignment)

