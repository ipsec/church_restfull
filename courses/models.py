from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200, blank=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class TeacherClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class StudentClass(models.Model):
    # owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.DateField()

    start_date = models.DateTimeField(verbose_name='Start Date', auto_now_add=True)
    end_date = models.DateTimeField(verbose_name='End Date', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.title
