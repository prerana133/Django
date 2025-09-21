from django.shortcuts import render,HttpResponse
from django.views import View
def show(request):
    return HttpResponse("heyy!!!!")
def display(request):
    return HttpResponse("hello!!!!")
class web(View):
    def get(self,request):
        return render(request,"web.html")
    