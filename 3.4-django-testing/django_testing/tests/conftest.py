import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory(student_factory):
    def factory(*args, **kwargs):
        students = student_factory(_quantity=2)
        return baker.make(Course, *args, **kwargs, students=students)
    return factory