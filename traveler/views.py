from django.shortcuts import render, redirect
from .forms import TravelerForm, TravelerEditForm
from .models import Traveler


def create_traveler(request):
    if request.method == "POST":
        form = TravelerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TravelerForm()

    return render(request, 'traveler/create-traveler.html', {'form': form})


def traveler_details(request):
    travelers = Traveler.objects.all()
    context = {
        'travelers': travelers,
    }

    return render(request, 'traveler/details-traveler.html', context)


def edit_traveler(request):
    traveler = Traveler.objects.first()
    if request.method == 'POST':
        form = TravelerEditForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('traveler_details')
    else:
        form = TravelerEditForm(instance=traveler)

    context = {
        'form': form,
    }
    return render(request, 'traveler/edit-traveler.html', context)


def delete_traveler(request):
    traveler = Traveler.objects.first()
    if request.method == 'POST':
        if traveler:
            traveler.delete()
        return redirect('home')

    return render(request, 'traveler/delete-traveler.html')


