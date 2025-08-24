from django.core.exceptions import ValidationError
import re

def validate_username(value):
    if not all(c.isalnum() or c == '_' for c in value):
        raise ValidationError('Invlid username character')
    if 5 > len(value):
        raise ValidationError('Too small username')


def validate_title(value):
    if not re.match(r'^[a-zA-Z0-9\s.,!?_"-]+$', value):
        raise ValidationError("Invalid title character")