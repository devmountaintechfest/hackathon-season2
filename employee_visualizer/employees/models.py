from django.db import models

class Employee(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 0
        FEMALE = 1

    class Status(models.IntegerChoices):
        ACTIVE = 1
        RESIGNED = 2
        RETIRED = 3

    emp_id = models.IntegerField()
    passport = models.TextField()
    firstname = models.TextField()
    lastname = models.TextField()
    gender = models.IntegerField(choices=Gender.choices)
    birthday = models.DateField()
    nationality = models.TextField()
    hired = models.DateField()
    dept = models.TextField()
    position = models.TextField()
    status = models.IntegerField(choices=Status.choices)
    region = models.TextField()

    def __str__(self):
        return self.emp_id