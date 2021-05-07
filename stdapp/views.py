from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def base(request):
    student=Student.objects.all()
    return render(request,'base.html',{'student':student})

def new(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('gender') and request.POST.get('mark'):
            student=Student()
            student.name= request.POST.get('name')
            student.gender= request.POST.get('gender')
            student.marks= request.POST.get('mark')
            student.save()
            return redirect('/')
    return render(request,'new.html')

def update(request,i):
    t = Student.objects.get(id=i)
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('gender') and request.POST.get('mark'):
            student=Student()
            student.name= request.POST.get('name')
            student.gender= request.POST.get('gender')
            student.marks= request.POST.get('mark')
            student.save()
            t.delete()
            return redirect('/')
    return render(request,'update.html',{'t':t})




def delete(request,i):
    d = Student.objects.get(id=i)
    d.delete()
    student=Student.objects.all()
    return redirect('/')

    
