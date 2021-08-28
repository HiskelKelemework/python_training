from django.db import models

# Create your models here.
class Question(models.Model):
    description = models.CharField(max_length=250)
    created_on = models.DateField()
    created_by = models.CharField(max_length=60)

    def __str__(self):
        return self.description

class Answer(models.Model):
    description = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Department(models.Model):
    name = models.CharField(max_length=100)
    

class Teacher(models.Model):
    name = models.CharField(max_length=60)
    degree_earned = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()
    instructors = models.ManyToManyField(Teacher)
    departments = models.ManyToManyField(Department)
