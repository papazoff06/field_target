from django.core.exceptions import ValidationError


def validate_competition_name(name):
    if not all(c.isalnum() or c.isspace() or c == "-" for c in name):
        raise ValidationError("The name must contain only letters, digits, and spaces")
validate_competition_name("Bansko Open 2025")