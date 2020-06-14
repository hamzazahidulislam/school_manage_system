from . import views
from django.urls import path
urlpatterns = [
    path('create/',views.create_teacher,name='create-teacher'),
    path('list/',views.teacher_list,name='teacher-list'),
    path('edit/<int:id>',views.edit_teacher,name='edit-teacher'),
    path('delete/<int:id>',views.delete_teacher,name='delete-teacher'),
    path('delete/<int:id>',views.delete_teacher,name='delete-teacher'),
]