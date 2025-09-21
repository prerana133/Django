from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path('',views.show,name='show'),
    path('show1',views.display,name='display'),
    path('web',views.web.as_view(),name='web'),
]
