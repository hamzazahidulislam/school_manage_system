from django import forms
from .models import StudentClassInfo,StudentShiftInfo,StudentInfo,StudentDetailInfo

class SearchStudentForm(forms.Form):
    student_class = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','id':'std_shift'}),queryset=StudentClassInfo.objects.all(),required=True)
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", 'id': 'roll'}),required=False)
    session = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", 'id': 'session'}),required=False)
#Student Registrations ('StudentRegistrationForm') With Form method
class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','id':'name'}),required=True)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control",'id':'age'}),required=True)
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", 'id': 'roll'}), required=True)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = forms.ChoiceField(choices=gender_choice,widget=forms.Select(attrs={'class':'form-control','id':'gender'}),required=True)
    father_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','id':'father_name'}),required=True)
    address = forms.CharField(max_length=50,widget=forms.Textarea(attrs={'class':'form-control','id':'address'}),required=True)
    std_class = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','id':'std_class'}),queryset=StudentClassInfo.objects.all(),required=True)
    std_shift = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control','id':'std_shift'}),queryset=StudentShiftInfo.objects.all(),required=True)
    std_section = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','id':'father_name'}),required=True)
    session = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control",'id':'session'}),required=True)

#Student Registrations Model Method But ('StudentInfoForm[1]')
class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = 'name','age','roll','gender','father_name','address',
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','id':'name','aria-required':"true"}),
            'age':forms.NumberInput(attrs={'class':'form-control','id':'age','aria-required':"true"}),
            'roll': forms.NumberInput(attrs={'class': 'form-control', 'id': 'roll', 'aria-required': "true"}),
            'gender':forms.Select(attrs={'class':'form-control','id':'gender','aria-required':"true"}),
            'father_name':forms.TextInput(attrs={'class':'form-control','id':'age','aria-required':"true"}),
            'address':forms.Textarea(attrs={'class':'form-control','id':'age','aria-required':"true"}),

        }
#Student Registrations Model Method But ('StudentDetailInfoForm[2]')
class StudentDetailInfoForm(forms.ModelForm):
    class Meta:
        model = StudentDetailInfo
        exclude = ('student',)
        fields ='std_class','std_shift','std_section','session'
        widgets ={
            'std_class': forms.Select(attrs={'class':'form-control','id':'std_class'}),
            'std_shift': forms.Select(attrs={'class':'form-control','id':'std_class'}),
            'std_section': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'aria-required': "true"}),
            'session': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'aria-required': "true"}),
        }