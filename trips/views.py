from django.shortcuts import render, redirect, get_object_or_404
from traveler.models import Traveler
from .forms import TripForm, DeleteTripForm
from .models import Trip


def create_trip_view(request):
    traveler = Traveler.objects.first()

    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.traveler = traveler
            trip.save()
            return redirect('all_trips')
    else:
        form = TripForm()

    return render(request, 'trips/create-trip.html', {'form': form})


def trip_details(request, trip_pk):
    trip = get_object_or_404(Trip, id=trip_pk)
    return render(request, 'trips/details-trip.html', {'trip': trip})


def edit_trip(request, trip_pk):
    trip = get_object_or_404(Trip, id=trip_pk)

    if request.method == "POST":
        form = TripForm(request.POST, request.FILES, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TripForm(instance=trip)

    return render(request, 'trips/edit-trip.html', {'form': form})


def delete_trip(request, trip_pk):
    trip = get_object_or_404(Trip, id=trip_pk)

    if request.method == 'POST':
        form = DeleteTripForm(request.POST, instance=trip)
        if form.is_valid():
            trip.delete()
            return redirect('all_trips')
    else:
        form = DeleteTripForm(instance=trip)

    return render(request, 'trips/delete-trip.html', {'form': form})
