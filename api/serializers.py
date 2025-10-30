from rest_framework import serializers
from .models import Employee, Role, Leave


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.first_name', read_only=True)

    class Meta:
        model = Leave
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name', read_only=True)
    leaves = LeaveSerializer(many=True, source='leave_set', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
