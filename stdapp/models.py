from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15)
    marks = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name