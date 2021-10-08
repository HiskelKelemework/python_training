from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)

        return Response(serializer.data)

    def post(self, request):
        deptData = request.data
        serializer = DepartmentSerializer(data=deptData)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=400)


class DepartmentsDetailView(APIView):
    def get(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(status=400)

    def delete(self, request, pk):
        department = Department.objects.get(pk=pk)
        serializer = DepartmentSerializer(department, data=request.data)

        department.delete()

        return Response(serializer.data)


def departments(request):
    # send back some html
    return render(request, 'departments.html', None)
