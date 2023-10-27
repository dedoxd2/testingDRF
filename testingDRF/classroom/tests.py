from django.test import TestCase
from . models import Student


class TestStudentModel(TestCase):
    def setUp(self):
        self.student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=12345)

    # setting up new users
    # getting access tokens / logged in users
    # setup timers

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a+b
        self.assertEqual(c, 3)

    def test_student_can_be_created(self):
        student_result = Student.objects.last()  # getting the last student
        self.assertEqual(self.student1, student_result)

    def test_str_return(self):

        # student1 = Student.objects.create(
        #     first_name="Tom", last_name="Jhon", admission_number=123)
        student_result = Student.objects.last()  # getting the last student
        self.assertEqual(self.student1.first_name, student_result.first_name)

    def test_grade_fail(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=1234, average_score=10)
        student_result = Student.objects.last()  # getting the last student
        self.assertEqual(student_result.get_grade(), "Fail")

    def test_grade_pass(self):
        student1 = Student.objects.create(
            first_name="Tom", last_name="Jhon", admission_number=1234, average_score=60)
        student_result = Student.objects.last()  # getting the last student
        self.assertEqual(student_result.get_grade(), "Pass")


def test_grade_Excellent(self):
    student1 = Student.objects.create(
        first_name="Tom", last_name="Jhon", admission_number=1234, average_score=80)
    student_result = Student.objects.last()  # getting the last student
    self.assertEqual(student_result.get_grade(), "Excellent")
