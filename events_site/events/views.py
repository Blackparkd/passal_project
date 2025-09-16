# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Location, Artist
from .forms import EventForm, LocationForm

def event_list(request):
    events = Event.objects.all()
    return render(request, "events/list.html", {"events": events})

def location_list(request):
    locations = Location.objects.all()
    return render(request, "events/locations/location_list.html", {"locations": locations})


def create_location(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("location_list")
    else:
        form = LocationForm()
    return render(request, "events/locations/create_location.html", {"form": form})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request, "events/events/create_event.html", {"form": form})