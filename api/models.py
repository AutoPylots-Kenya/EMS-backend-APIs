from django.db import models
from cloudinary.models import CloudinaryField


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    profile_picture = CloudinaryField('image', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    cv = CloudinaryField('file', resource_type='raw', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    approval = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}"