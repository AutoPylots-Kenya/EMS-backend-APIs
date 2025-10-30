from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, RoleViewSet, LeaveViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('roles', RoleViewSet)
router.register('leaves', LeaveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]