from django.db import models


class Teacher(models.Model):
    first_name = models.TextField()
    patronymic = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Subject(models.Model):
    name = models.TextField()
    semester = models.IntegerField()
    teachers = models.ManyToManyField(Teacher, related_name='subjects')

    def __str__(self):
        return self.name
