from django.shortcuts import render

# Create your views here.
def index(request):
    # context is sending information from backend to frontend
    # context is dictionary type which store in the form of key and value pair
    context = {
        'name' : 'prerana',
        'age' : 23,
        'course' : 'python full stack'
    }
    return render(request,'index.html',context) 

from myapp.models import Student

def students(request):
    context = {
        'students' : Student.objects.all()
    }
    return render(request,'students.html',context)