from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import employee



def home(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('register')

        else:
            messages.error(request,'please check username or password or sign in ')
            redirect('home')

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        Email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        if User.objects.filter(username=username).exists():
            messages.error(request,'this username already exist login with  this username or use another username to create account ')
            return redirect('signup')

        if pass1!=pass2:
            messages.error(request,'both password doesn,t match')
            return redirect('signup')

        else:
            user_data = User.objects.create_user(username, Email, pass1)
            user_data.save()
            messages.success(request,'your account successfully created')
            return redirect('home')


    return render(request,'signup.html')

@login_required(login_url='home')
def register(request):
    if request.method=='POST':
        name=request.POST['fname']
        lname=request.POST['lname']
        gender =request.POST['gender']
        date=request.POST['date']
        partment=request.POST['department']



        obj=employee(fname=name,lname=lname,gender=gender,date=date,department=partment)
        obj.save()
        return redirect('employeedata')

    return render(request, 'register.html')

@login_required(login_url='home')
def data(request):
    empdata=employee.objects.all()
    return render(request,'data.html',context={'data': empdata})

def deleteme(request,id):
    obj=employee.objects.get(id=id)
    obj.delete()
    empdata=employee.objects.all()
    return render(request,'data.html',context={'data': empdata})

def editme(request,id):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        gender=request.POST['gender']
        date=request.POST['date']
        department=request.POST['department']

        obj = employee.objects.get(id=id)

        obj.fname=fname
        obj.lname=lname
        obj.gender=gender
        obj.date=date
        obj.department=department
        obj.save()
        return redirect('employeedata')

    obj=employee.objects.get(id=id)
    return render(request, 'edit.html', context={'data': obj})

def loggout(request):
    logout(request)
    return redirect('home')











