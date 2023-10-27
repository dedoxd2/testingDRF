from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admission_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.first_name

    def get_grade(self):
        if self.get_grade < 40:
            return "Fail"
        elif 40 < self.get_grade < 70:
            return "Pass"
        elif 70 < self.get_grade < 100:
            return " Excellent"
        else:
            return "Error"


class Classroom(models.Model):
    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    # students = models.ManyToManyField()

    def __str__(self):
        return self.name
