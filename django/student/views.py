from django.db.models import Q
from django.shortcuts import render

# Create your views here.

from rest_framework import mixins, generics, status
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from student.models import Student
from student.serializers import StudentSerializer


class StudentListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get("q")
        if query:
            self.queryset = self.queryset.filter(Q(student_name__icontains=query))
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class StudentCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_201_CREATED, "message": "student data created successfully"})
        return Response(serializer.errors, status=status.HTTP_200_OK)


class StudentDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, pk):
        obj = Student.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"status": status.HTTP_200_OK, "message": "Record Does Not Exist"})
        else:
            return obj

    def get(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj)
        return Response(serializer.data)


class StudentUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, pk):
        obj = Student.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"status": status.HTTP_204_NO_CONTENT, "message": "Record does not exist"})
        else:
            return obj

    def put(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_202_ACCEPTED, "message": "student data updated successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_object(self, pk):
        obj = Student.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"status": status.HTTP_404_NOT_FOUND, "message": "requeted object not found in model"})
        else:
            return obj

    def delete(self,request, pk=None):
        try:
            obj = self.get_object(pk)
            obj.delete()
            return Response({"status": status.HTTP_202_ACCEPTED, "message": "object deleted successfully"})

        except Exception as e:
            print(e)
            return Response({"status": status.HTTP_200_OK, "message": "object not deleted "})
