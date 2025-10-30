from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Employee, Role, Leave
from .serializers import EmployeeSerializer, RoleSerializer, LeaveSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'email', 'role__name']
    ordering_fields = ['first_name', 'last_name', 'email']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.select_related('employee').all()
    serializer_class = LeaveSerializer
