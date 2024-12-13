from django.db import models
from .validators import DestinationValidator


class Trip(models.Model):
    destination = models.CharField(
        max_length=100,
        validators=[DestinationValidator()],
    )
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(
        default=1,
        help_text="*Duration in days is expected."
    )
    image_url = models.URLField(
        blank=True,
        null=True
    )
    traveler = models.ForeignKey(
        'traveler.Traveler',
        on_delete=models.CASCADE,
        related_name='trips',
        editable=False
    )

    def __str__(self):
        return self.destination
