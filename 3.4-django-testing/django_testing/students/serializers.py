from urllib import request
from rest_framework import serializers
from django_testing.settings import MAX_STUDENTS_PER_COURSE

from students.models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")

    def validate(self, data):
        students = data.get("students")
        if  type(students)==list and len(students) >= MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError(
                f"Only {MAX_STUDENTS_PER_COURSE} students allowed in course"
                )
        return data

            