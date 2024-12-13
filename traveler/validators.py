from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class NicknameValidator:
    def __init__(self, message=None):
        self.message = message or "Your nickname is invalid!"

    def __call__(self, value):
        if not (3 <= len(value) <= 30):
            raise ValidationError("Your nickname must be between 3 and 30 characters long.")
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise ValidationError(self.message)


@deconstructible
class CountryCodeValidator:
    def __init__(self, message=None):
        self.message = message or "The country code must consist of exactly 3 characters."

    def __call__(self, value):
        if len(value) != 3:
            raise ValidationError(self.message)
