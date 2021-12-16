from django.db import models


class Student(models.Model):
    student_id = models.CharField(max_length=250)
    student_name = models.CharField(max_length=250)
    student_city = models.CharField(max_length=250)
    student_course = models.CharField(max_length=250)

    def __str__(self):
        return self.student_name
