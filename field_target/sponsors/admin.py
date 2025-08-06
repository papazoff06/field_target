from django.contrib import admin

from field_target.sponsors.models import Sponsor


# Register your models here.
@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass