from . import views
from django.urls import path
urlpatterns = [
    path('employee/create',views.create_employee,name='create-employee'),
]