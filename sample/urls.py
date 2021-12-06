from django.contrib import admin
from django.urls import path, include
from employee.views import EmployeeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'api/employee', EmployeeViewSet, basename='Employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('auth.urls')),
    path('', include(router.urls)),
]

