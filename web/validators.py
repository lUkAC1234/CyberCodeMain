from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

def lowercase_letters_username_validator(value):
    if not value.islower() or not value.isalpha() or len(value) < 8 or len(value) > 16:
        raise ValidationError(
            _('Username can only contain lowercase English letters (a-z) and must be between 8 and 16 characters long.')
        )
