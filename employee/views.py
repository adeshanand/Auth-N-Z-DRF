import xlwt

from . import models
from . import serializers
from .utils import *

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Employee.objects.filter(creator=self.request.user.id)

    def create(self, request):
        data = request.data
        data['creator'] = self.request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        data = request.data
        data['creator'] = self.request.user.id
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def export_xl(self, request):
        """ Export employee in excel format """
        try:
            emp_export = models.Employee.objects.filter(creator=self.request.user.id)
            return export_excel(emp_export)
        except Exception as e:
            return Response({"error": "Something went wrong"}, status=400)
    
    @action(detail=False, methods=['get'])
    def export(self, request):
        """ Export employee in csv format """
        try:
            emp_export = models.Employee.objects.filter(creator=self.request.user.id)
            return export_csv(emp_export)
        except Exception as e:
            return Response({"error": "Something went wrong"}, status=400)
        