from django.contrib import admin
from .models import Question, Answer, Course, Department, Teacher
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Teacher)

'''
    1. create a new folder
    2. create a new python environment
    3. install django
    4. create a new django project

    5. create a new application called ecommerce
        - make sure to connect the new app to the root app.
    6. create the models necessary (customer, item, order)
        N.B: a single order can have multiple items.
             an item can be included in multiple orders
    7. make the neccesary migrations and apply them
    8. add the models you created to the admin site
'''
