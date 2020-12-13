from django.shortcuts import render
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class EmployeeCRUDCBV(ModelViewSet):
    authentication_classes = [SessionAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
