from django.contrib import admin
from .models import Question, Answer, Course, Department, Teacher
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Teacher)
