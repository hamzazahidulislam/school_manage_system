from django.shortcuts import render,redirect
from django.contrib import messages
from .models import StudentInfo,StudentDetailInfo
from .form import StudentRegistrationForm,SearchStudentForm,StudentDetailInfoForm,StudentInfoForm

def attendance_count(request):
    class_name = request.GET.get("class_name",None)
    if class_name:
        std_list = StudentDetailInfo.objects.filter(std_class__class_short_form=class_name).order_by('student__roll')
        context = {'std_list':std_list}
    else:
        context = {}
    return render(request,'student/att_count.htm',context)

def search_student(request):
    forms = SearchStudentForm()
    std_class = request.GET.get("student_class",None)
    roll = request.GET.get("roll",None)
    session = request.GET.get("session",None)
    if std_class:
        students = StudentDetailInfo.objects.filter(std_class__id=std_class)
        if roll:
            students = students.filter(student__roll=roll)
        if session:
            students = students.filter(session=session)
        context = {'forms': forms,'students': students}
        return render(request, 'student/std_search.htm', context)


    context = {'forms':forms}
    return render(request,'student/std_search.htm',context)
#Student Registration (create_student) With Form method
def create_student(request):
    forms = StudentRegistrationForm()
    if request.method == 'POST':
        forms = StudentRegistrationForm(request.POST)
        if forms.is_valid():
                messages.success(request, "Your Data Insert Successfully!")
                std_name = forms.cleaned_data['name']
                std_age = forms.cleaned_data['age']
                roll = forms.cleaned_data['roll']
                std_gender = forms.cleaned_data['gender']
                father_name = forms.cleaned_data['father_name']
                address = forms.cleaned_data['address']
                std_class = forms.cleaned_data['std_class']
                std_shift = forms.cleaned_data['std_shift']
                std_section = forms.cleaned_data['std_section']
                session = forms.cleaned_data['session']
                std_obj = StudentInfo.objects.create(
                    name=std_name,
                    age=std_age,
                    roll=roll,
                    gender=std_gender,
                    father_name=father_name,
                    address=address,
                )
                StudentDetailInfo.objects.create(
                    student=std_obj,
                    std_class=std_class,
                    std_shift=std_shift,
                    std_section=std_section,
                    session=session
                )
                return redirect('student-list')
    context = {'forms': forms}
    return render(request, 'student/create_std.htm',context)

def student_list(request):
    student_list = StudentDetailInfo.objects.all()
    context = {'student_list': student_list}
    return render(request,'student/student_list.htm',context)

def detail_class(request,class_name):
    class_name = StudentDetailInfo.objects.filter(std_class__class_name=class_name)
    print(class_name)
    #student_filter_by_class

    context = {'detail_class': class_name}
    return render(request,'student/student_list_by_class.htm',context)

def student_detail(request,id):
    std_detail_obj = StudentInfo.objects.get(id=id)
    context = {'student_detail': std_detail_obj}
    return render(request,'student/student_detail.htm',context)

# def edit_student(request,id):
#     std_obj = StudentInfo.objects.get(id=id)
#     forms = StudentRegistrationForm(instance=std_obj)
#     if request.method == "POST":
#         forms = StudentRegistrationForm(request.POST,instance=std_obj)
#         if forms.is_valid():
#             forms.save()
#             return redirect('student-list')
#     context = {'forms':forms}
#     return render(request,'student/edit_student.htm',context)

def edit_student(request,id):
    std_obj = StudentDetailInfo.objects.get(student__id=id)
    print("student id object",std_obj)
    student_info = std_obj.student
    form1 = StudentInfoForm(request.POST or None ,instance=student_info)
    form2 = StudentDetailInfoForm(request.POST or None,instance=std_obj)
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student = std_obj
            std_detail.save()
            return redirect('student-list')
    context = {'form1': form1,'form2':form2}
    return render(request, 'student/edit_student.htm', context)

def std_delete(request,id):
    std_obj = StudentInfo.objects.get(id=id)
    std_obj.delete()
    return redirect('student-list')
#Student Registration (register_student) With Form Model Method
def register_student(request):
    form1 = StudentInfoForm(request.POST or None)
    form2 = StudentDetailInfoForm(request.POST or None)
    if request.method == 'POST':
        if form1.is_valid() and form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student = std_obj
            std_detail.save()
            return redirect('student-list')
    context = {'form1': form1 , 'form2':form2}
    return render(request,'student/register_student.htm',context)
