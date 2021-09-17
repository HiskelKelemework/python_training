from django.urls import path
from .views import DepartmentListView, DepartmentsDetailView

urlpatterns = [
    path('departments/', DepartmentListView.as_view()),
    path('departments/<int:pk>', DepartmentsDetailView.as_view()),
]
