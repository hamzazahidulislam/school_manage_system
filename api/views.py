from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from student.models import *
from .serializers import ResultSerializer,StudentInfoSerializer
from student.models import Result,StudentInfo


class StudetnDetail(APIView):
    def get(self,request,id):
        student_detail = StudentInfo.objects.get(id=id)
        student_serializer = StudentInfoSerializer(student_detail)
        return Response({'status': student_serializer.data}, status=status.HTTP_200_OK)

class StudentInfoView(APIView):
    def get(self,request):
        students = StudentInfo.objects.all()
        student_serializer = StudentInfoSerializer(students,many=True)
        return Response({'status': student_serializer.data}, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = StudentInfoSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success'},status=status.HTTP_200_OK)
        return Response({'status':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view()
def std_attendance(request,std_cls,std_roll):
    try:
        Attendance.objects.create_attendance(std_cls,std_roll)
        return Response({'status':'success'},status=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return Response({'status': 'failed'},status=status.HTTP_400_BAD_REQUEST)

class StudentAttendance(APIView):
    def get(self,request,std_cls,std_roll):
        try:
            Attendance.objects.create_attendance(std_cls, std_roll)
            return Response({'status': 'success'}, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'status': 'failed'}, status=status.HTTP_400_BAD_REQUEST)

class ResultView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.data)
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            board = serializer.validated_data["board"]
            roll = serializer.validated_data["roll"]
            result_obj = Result.objects.get(board=board,roll=roll)
            return Response({'result': result_obj.gpa}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)