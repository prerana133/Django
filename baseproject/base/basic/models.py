from django.db import models



class students(models.Model):
    name=models.CharField(max_length=40)
    course=models.CharField(max_length=20)
    age=models.IntegerField()
    


