from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Person
from meetings.models import Meeting


# Create your views here.

def home(request):
    person = Person('Techie Frankie', 27)
    view_model = dict(msg=f'This dynamic information was generated on {datetime.now()}',
                      meeting_count=Meeting.objects.count(), name=person.name, age=person.age)

    return render(request, 'webapp/home.html', {'meetings': Meeting.objects.all()})
