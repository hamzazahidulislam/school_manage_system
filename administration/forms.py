from django import forms
from .models import Employee
class EmployeeCreateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'username','aria-required':"true"}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','aria-required':"true"}),required=True)
    class Meta:
        model = Employee
        fields = ('username','password','name','mobile','designation')
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','id':'name','aria-required':"true"}),
            'mobile':forms.TextInput(attrs={'class':'form-control','id':'mobile','aria-required':"true"}),
            'designation':forms.Select(attrs={'class':'form-control','id':'destination','aria-required':"true"})
        }