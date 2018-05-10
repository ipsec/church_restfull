from django.contrib import admin

# Register your models here.
from courses.models import StudentClass
from courses.models import Student
from courses.models import Teacher
from courses.models import TeacherClass
from courses.models import Course

admin.site.register(StudentClass)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(TeacherClass)
admin.site.register(Course)
