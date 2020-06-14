from . import views
from django.urls import path
urlpatterns = [
    path('attendance/<std_cls>/<std_roll>', views.StudentAttendance.as_view(), name='delete-std'),
    path('result',views.ResultView.as_view(),name='result'),
    path('studentinfo/',views.StudentInfoView.as_view(),name="create-student-in-api"),
    path('student-detail/<int:id>',views.StudetnDetail.as_view(),name="student-detail-in-api"),
]