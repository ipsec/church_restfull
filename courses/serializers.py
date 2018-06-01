from rest_framework import serializers

from courses.models import StudentClass, Course, Student, Teacher


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'
