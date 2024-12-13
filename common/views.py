from django.shortcuts import render

from traveler.models import Traveler
from trips.models import Trip


def home_view(request):
    return render(request, 'common/index.html')


def all_trips_view(request):
    traveler = Traveler.objects.first()
    trips = Trip.objects.filter(traveler=traveler) if traveler else []

    context = {
        'trips': trips,
        'traveler': traveler,
    }
    return render(request, 'common/all-trips.html', context)



