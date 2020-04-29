from django.shortcuts import render, get_object_or_404, redirect
from .models import Meeting
from django.forms import modelform_factory
from .forms import MeetingForm

from setup import get_logger


# Create your views here.
def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


# create a new model form for creating new meeting form
# MeetingForm = modelform_factory(Meeting, exclude=[])


def schedule(request):
    if request.POST:
        # process submitted form
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            get_logger().info("Successfully saved scheduled to the database")
            return redirect('home')
    else:
        form = MeetingForm()
    # display empty form if new request  or filled form with error messages when an invalid was submitted
    return render(request, 'meetings/schedule.html', {'form': form})
