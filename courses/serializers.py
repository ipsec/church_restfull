from rest_framework import serializers

from courses.models import Class


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ('title', 'text')