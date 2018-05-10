from rest_framework import serializers

from courses.models import StudentClass


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('title', 'text')