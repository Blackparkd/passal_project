from django.urls import path
from .views import event_list, location_list, create_location, create_event

urlpatterns = [
    path("", event_list, name="event_list"),
    path("locations/", location_list, name="location_list"),
    path("locations/create/", create_location, name="create_location"),
    path("events/create/", create_event, name="create_event"),  # New URL pattern for creating events
]