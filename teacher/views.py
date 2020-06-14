from django.shortcuts import render,redirect
from .form import TeacherForm
from .models import TeacherInfo
from django.contrib import messages

def delete_teacher(request,id):
    teacher_obj = TeacherInfo.objects.get(id=id)
    teacher_obj.delete()
    return redirect('teacher-list')

def edit_teacher(request,id):
    teacher_obj = TeacherInfo.objects.get(id=id)
    print(teacher_obj)
    forms = TeacherForm(instance=teacher_obj)
    if request.method == 'POST':
        forms = TeacherForm(request.POST,instance=teacher_obj)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your Data Update Successfully!")
            return redirect('teacher-list')
        else:
            messages.error(request,"Your Data NOT Updated? ")
    context = {'forms': forms}
    return render(request, 'teacher/edit_teacher.htm',context)
def create_teacher(request):
    forms = TeacherForm()
    if request.method == 'POST':
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your Data Insert Successfully!")
            return redirect('teacher-list')
        else:
            messages.error(request,"this user name already exixts ")
    context = {'forms': forms}
    return render(request, 'teacher/create_teacher.htm', context)

def teacher_list(request):
    teacher_list = TeacherInfo.objects.all()
    context = {"teacher_list": teacher_list}
    return render(request, 'teacher/teacher_list.htm',context)