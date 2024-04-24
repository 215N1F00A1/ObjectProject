from django.http import HttpResponse
from django.shortcuts import render

from objectapp.models import Student


# Create your views here.
def home(request):
    name = "veena"
    age = 25
    place = "bangalore"
    marks = 95
    s1 = Student(name, age, place, marks)
    context = {'s1': s1}
    return render(request, 'display.html', context)
    return HttpResponse(f"my name is {s1.name} <br> my age is {s1.age} <br> my place is {s1.place}"
                        f" <br> my marks is {s1.marks}")


def practice_fun(request):
    name=request.POST['name']
    age=int(request.POST.get('age'))
    place=request.POST['place']
    marks=int(request.POST.get('marks'))

    data={'name':name,'age':age,'place':place,'marks':marks}

    return render(request,'practice.html',data)