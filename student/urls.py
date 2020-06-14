from . import views
from django.urls import path

urlpatterns = [
    path('create/',views.create_student,name='create-student'),
    path('register/',views.register_student,name='register-student'),
    path('list/',views.student_list,name='student-list'),
    path('class/detail/<str:class_name>', views.detail_class, name='detail-classes'),
    path('search/', views.search_student, name='search-student'),
    path('detail/<int:id>', views.student_detail, name='student-detail'),
    path('edit/<int:id>', views.edit_student, name='edit-student'),
    path('delete/<int:id>', views.std_delete, name='delete-std'),
    path('att-count', views.attendance_count, name='att-count'),
]