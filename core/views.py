
# Create your views here.
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer
from polls.paginations import CustomPagination


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    pagination_class = CustomPagination