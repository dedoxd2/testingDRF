from django.test import TestCase
from . models import Student, Classroom
from mixer.backend.django import mixer
import pytest


pytestmark = pytest.mark.django_db


class TestStudentModel(TestCase):
    # def setUp(self):
    #      self.student1 = Student.objects.create(
    #          first_name="Tom", last_name="Jhon", admission_number=12345)
    ##########################
    # u can initialize variables here and use it in functions
    # setting up new users
    # getting access tokens / logged in users
    # setup timers

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a+b
        # self.assertEqual(c, 3)
        assert c == 3

    def test_student_can_be_created(self):
        student1 = mixer.blend(Student, first_name="dedo")
        student_result = Student.objects.last()  # getting the last student

        assert student_result.first_name == "dedo"

    def test_str_return(self):
        # student1 = Student.objects.create(
        #     first_name="Tom", last_name="Jhon", admission_number=123)

        student1 = mixer.blend(Student)
        student_result = Student.objects.last()  # getting the last student
        self.assertEqual(student1.first_name, student_result.first_name)

    def test_grade_fail(self):
        student1 = mixer.blend(Student, average_score=10)
        student_result = Student.objects.last()
        # self.assertEqual(student_result.get_grade(), "Fail")
        assert student_result.get_grade() == "Fail"

    def test_grade_pass(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=1234, average_score=60)
        student_result = Student.objects.last()
        assert student_result.get_grade() == "Pass"

    def test_grade_Excellent(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=1234, average_score=80)
        student_result = Student.objects.last()
        assert student_result.get_grade() == "Excellent"

    def test_grade_Error(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=1234, average_score=101)
        student_result = Student.objects.last()
        assert student_result.get_grade() == "Error"


class TestClassroomModel:
    def test_classroom_create(self):
        classroom = mixer.blend(Classroom, name="Physics")
        classroom_result = Classroom.objects.last()  # getting the last student
        assert classroom_result.name == "Physics"
        assert str(classroom_result) == "Physic"
