from django import forms
from .models import TeacherInfo
class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control error','id':'name'}),
            'gender' : forms.Select(attrs={'class':'form-control','id':'gender'}),
            'phone_number' : forms.TextInput(attrs={'class':'form-control','id':'phone_number'}),
            'destination' : forms.TextInput(attrs={'class':'form-control','id':'destination'})
        }