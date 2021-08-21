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