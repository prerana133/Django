from django.shortcuts import render,redirect
from crud.models import details

def readall(request):
    if request.method=="POST":
        name=request.POST.get("name")
        course=request.POST.get("course")
        age=request.POST.get("age")
        details.objects.create(name=name,course=course,age=age)


    context={

           'information' : details.objects.all()
        }
    return render(request,'student.html',context)

def updateall(request,id):
    student=details.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        course=request.POST.get("course")
        age=request.POST.get("age")

        student.name=name
        student.course=course
        student.age=age
        student.save()

        return redirect("readall")
    

    context={
        'student':student
    }
    
    return render(request,"update.html",context)

def delete(request,id):
    stu=details.objects.get(id=id)
    stu.delete()
     
    return redirect("readall")