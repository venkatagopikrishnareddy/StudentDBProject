from django.shortcuts import render
from StudentDBApp.models import Student

#Create your views here.
def studentview(request):
    studentlist = Student.objects.order_by('marks')		#def-order is ASC-order (DJ-ORM-code)
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);


from django.shortcuts import render
from StudentDBApp.models import Student

#Create your views here.
def studentview(request):		#old
    studentlist = Student.objects.order_by('marks')
    dict1={'studentlist':studentlist}
    return render(request,'StudentDBApp/students.html',context=dict1);


from StudentDBApp.models import Student2;
def student_homepage(request):				#new
    students= Student2.objects.all()
    students=Student2.objects.filter(marks__lt=35)
    #students=Student2.objects.filter(name__startswith='A')
    #students=Student2.objects.all().order_by('marks')  #ASC
    students=Student2.objects.all().order_by('-marks')   #DESC
    return render(request, 'StudentDBApp/index.html', {'students':students})

from StudentDBApp.models import Student1
def studentdata(request):
    studlist=Student1.objects.all()
    dict1={'studlist':studlist}
    return render(request, 'StudentDBApp/student.html', context=dict1);