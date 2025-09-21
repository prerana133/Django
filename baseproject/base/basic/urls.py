from django.urls import path
from basic import views

urlpatterns=[
    path('index',views.index),
    path('show',views.show),
]