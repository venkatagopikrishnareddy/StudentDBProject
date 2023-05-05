from django.db import models
#Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()

class Student2(models.Model):       #Faker-data
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)        #single-line-text
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    address=models.TextField()          #multi-line-text

#(sno,sname,clgname,course,marks)
from django.db import models
class Student1(models.Model):
    sno= models.IntegerField();
    sname=models.CharField(max_length=50);
    course=models.CharField(max_length=20);
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    sub3 = models.IntegerField()
    sub4 = models.IntegerField()
    sub5 = models.IntegerField()
    def total(self):
        return self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
    def avg(self):
        return self.total()/5
    def grade(self):
        avg=self.avg()
        if avg>=90:
            return 'A'
        elif avg>=75:
            return 'B'
        elif avg>=60:
            return 'C'
        elif avg>=45:
            return 'D'
        else:
            return 'Fail'
    def __str__(self):
        return 'Student1 object with sno:'+str(self.sno);
