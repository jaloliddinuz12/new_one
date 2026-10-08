
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.viewsets import ModelViewSet

from . import permissions
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework import authentication



class StudentListAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs.get("course_id")
        if course_id:
            students = self.queryset.filter(course_id=course_id)
        else:
            students = self.queryset.all()
        return students

    def get_serializer_class(self):
        # if self.request.user.is_staff:
        #     return StudentSerializerForAdmin
        return self.serializer_class


class StudentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = "student_id"
    permission_classes = [IsAdminOrReadOnly]




class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [
        # authentication.BasicAuthentication,
        authentication.SessionAuthentication
    ]

class StudentViewSet(ModelViewSet):
    def get_queryset(self):
        return Student.objects.all()
    def get_serializer_class(self):
        return StudentSerializer

    lookup_field = "pk"
    lookup_url_kwarg = None