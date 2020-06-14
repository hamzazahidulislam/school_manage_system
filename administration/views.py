from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EmployeeCreateForm

def create_employee(request):
    forms = EmployeeCreateForm()
    if request.method == 'POST':
        forms = EmployeeCreateForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user_obj = User.objects.create_user(username=username,password=password)
            new_user = forms.save(commit=False) # create user object variable
            new_user.user = user_obj #new user objects
            new_user.save()# user saved
            print("ok")
            return redirect('home')

    context = {'forms': forms}
    return render(request, 'administration/create_employee.htm', context)

