from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def indexview(request):
    context={
        'user':request.user
    }

    return render(request,"index.html",context)


def Loginuser(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        user= authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            message='username or password is incorrect'
    context={
        "message": message
    }

    return render(request,'login.html',context)


def SignupUser(request):
    message=''
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        p1=request.POST.get('password')
        p2=request.POST.get('confirmpassword')

        if p1==p2:
           try:
               user=User.objects.create_user(username,email,p1)
               user.save()
               return redirect ('login')
           except Exception 