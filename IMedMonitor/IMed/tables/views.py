from django.shortcuts import render
from django.http import HttpResponse
from models import Person 


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def people(request):
    return render(request, "people.html", {"people": Person.objects.all()})
    table = Person(data)