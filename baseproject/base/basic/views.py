from django.shortcuts import render


# Create your views here.
def index(request):
     context={
        'name':'prerana',
        'age': 22,
        'course':'python'
             }
     return render(request,'index.html',context)

from basic.models import students
def show(request):
     context={
          'student':students.objects.all()
     }
     return render(request,"show.html",context)