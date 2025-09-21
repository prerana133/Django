from django.shortcuts import render,redirect
from t1.models import Student
def show(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")

        Student.objects.create(name=name,email=email,phone=phone)
    context={
        'details':Student.objects.all()
    }
    return render(request,'index.html',context)
def update(request,id):
    stu=Student.objects.get(id=id)
    if request.method=="POST":
      name=request.POST.get("name")
      email=request.POST.get("email")
      phone=request.POST.get("phone")


      stu.name=name
      stu.email=email
      stu.phone=phone
      stu.save()

      return redirect('index')
    
    context={
       "stu":stu
    }

    return render(request,"index.html",context)
    
def delete(request,id):
  student=Student.objects.get(id=id)
  student.delete()
  return redirect("index")

