from django.shortcuts import render

from django.http import HttpResponse

from MyApp.models import Emp
from MyApp.forms import EmpForm

from MyApp.forms import EmpModelForm
from django.http import HttpResponseRedirect

from django.core.mail import send_mail

def Hello(request):
    return HttpResponse("Hello python")


def ShowEmpDetails(request):
   records=Emp.objects.all()
   return render(request,'index.html',{'rec':records})




	#return render(request,'index.html',{'id':1002,'name':'dhoni','salary':100000})

def eForm(request):
    if request.method=='POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            eid=form.cleaned_data['eid']
            ename=form.cleaned_data['ename']
            dob=form.cleaned_data['dob']
            email=form.cleaned_data['email']
            print(eid,ename,dob,email)

    form=EmpForm()
    return render(request,'temp.html',{'form':form})
    

def eFormdetails(request):
    if request.method=='POST':
        form=EmpModelForm(request.POST)
        if form.is_valid():
            form.save()
            
        return HttpResponseRedirect("http://127.0.0.1:8000/admin")



    form=EmpModelForm()
    return render(request,'temp.html',{'form':form})


def sendmail(request):
    send_mail('hello','registration successful','porur.besant@gmail.com',['anushaskonhett3@gmail.com'],fail_silently = False)
    return render(request,'index.html')



    
    









