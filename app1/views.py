from django.shortcuts import render
from app1 import forms
def Empview(request):
    form=forms.EmpForm()
    return render(request,'app1/welcome.html',{'form':form})

# Create your views here.
