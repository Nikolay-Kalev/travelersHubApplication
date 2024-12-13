from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class DestinationValidator:
    def __init__(self, message=None):
        self.message = message or "The destination must be between 3 and 100 characters long."

    def __call__(self, value):
        if not (3 <= len(value) <= 100):
            raise ValidationError(self.message)

