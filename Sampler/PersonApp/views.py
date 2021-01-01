from django.shortcuts import render
from .models import Person

def person(request):
    return render(request,'person.html',{"person":Person.objects.all()})