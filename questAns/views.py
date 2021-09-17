from rest_framework.views import APIView
from rest_framework.response import Response
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
            return Response('department list view post response works')


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

        return Response('update failed')
