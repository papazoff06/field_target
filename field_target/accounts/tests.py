import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from field_target.competitions.models import Competition


# Create your tests here.
class CompetitionTests(TestCase):
    def test_competition_with_valid_name_data(self):
        name = "Bansko Open 2025"
        c = Competition(
            name=name,
            start_date="2025-01-01",
            end_date="2025-12-31",
            location="Bansko",
            description="Yahooo!!!",
        )

        c.full_clean()
        c.save()

        self.assertIsNotNone(c)

    def test_competition_with_invalid_name_data(self):
        name = "~Bansko Open 2025~"
        c = Competition(
            name=name,
            start_date="2025-01-01",
            end_date="2025-12-31",
            location="Bansko",
            description="Yahooo!!!",
        )

        with self.assertRaises(ValidationError):
            c.full_clean()
