from traveler.models import Traveler


def get_traveler(request):
    return {
        'traveler': Traveler.objects.first(),
    }