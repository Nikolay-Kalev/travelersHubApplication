from django.db import models
from .validators import NicknameValidator, CountryCodeValidator


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[NicknameValidator()],
        help_text="*Nicknames can contain only letters and digits."
    )
    email = models.EmailField(
        max_length=30,
        unique=True
    )
    country = models.CharField(
        max_length=3,
        validators=[CountryCodeValidator()]
    )
    about_me = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nickname
    