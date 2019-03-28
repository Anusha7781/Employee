from django import forms
from MyApp.models import Emp

class EmpForm(forms.Form):
        eid=forms.CharField()
        ename=forms.CharField()
        dob=forms.DateTimeField()
        email=forms.EmailField()
	#course=forms.ChoiceField(choices=[('c c++','c c++'),('java','java'),('python','python')])
	#address=forms.CharField()
        

class EmpModelForm(forms.ModelForm):
        class Meta:
                model=Emp
                fields=('eid','ename','dob','email')
