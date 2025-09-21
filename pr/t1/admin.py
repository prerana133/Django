from django.contrib import admin
from t1.models import Student
class p1_admin(admin.ModelAdmin):
    list_display=['name','email','phone']
    list_filter=['name']
    list_editable=['phone']
    search_fields=['name','email','phone']
    ordering=['id']
admin.site.register(Student,p1_admin)


# Register your models here.
