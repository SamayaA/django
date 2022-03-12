from django.test import RequestFactory
import pytest
from django.contrib.auth.models import User
from model_bakery import baker

from students.models import Course, Student

@pytest.mark.django_db
def test_get_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=1)

    #Act
    responce = client.get("/api/v1/courses/1/")
    data = responce.json()

    #Assert
    assert responce.status_code == 200
    assert data["name"] == courses[0].name
    assert data["id"] == 1


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    #Arrange
    count = Course.objects.count()
    quantity = 2
    courses = course_factory(_quantity=quantity)

    #Act
    responce = client.get("/api/v1/courses/")
    data = responce.json()

    #Assert
    assert responce.status_code == 200
    assert Course.objects.count() == count + quantity
    for i, course in enumerate(data):
        assert course["name"] == courses[i].name


#test the filtration by id
@pytest.mark.django_db
def test_get_filter_id_courses(client, course_factory):
    #Arrange
    quantity = 2
    courses = course_factory(_quantity=quantity)

    #Act
    responce = client.get("/api/v1/courses/?id=4")
    data = responce.json()

    #Assert
    assert responce.status_code == 200
    assert data[0]["id"] == courses[0].id
    assert data[0]["name"] == courses[0].name


#test the filtration by name
@pytest.mark.django_db
def test_get_filter_name_courses(client, course_factory):
    #Arrange
    quantity = 2
    courses = course_factory(_quantity=quantity)
    
    #Act
    responce = client.get(f"/api/v1/courses/?name={courses[0].name}")
    data = responce.json()

    #Assert
    assert responce.status_code == 200
    assert data[0]["id"] == courses[0].id
    assert data[0]["name"] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    #Arrange
    c_data = {
        "name": "alg",
        "students": []
    }
    #Act
    responce = client.post("/api/v1/courses/", data=c_data, format='json')

    #Assert
    assert responce.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=3)
    data = {
        "name": "alg",
        "students": []
    }
    some_id = courses[0].id
    #Act
    responce_before = client.get(f"/api/v1/courses/{some_id}/")
    responce = client.patch(f"/api/v1/courses/{some_id}/", data=data, format='json')
    #Assert
    assert responce_before.status_code == 200
    assert responce.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=4)
    some_id = courses[0].id
    #Act
    responce_before = client.get(f"/api/v1/courses/{some_id}/")
    responce = client.delete(f"/api/v1/courses/{some_id}/")
    responce_after = client.get(f"/api/v1/courses/{some_id}/")
    #Assert
    assert responce_before.status_code == 200
    assert responce.status_code == 204
    assert responce_after.status_code == 404

    







