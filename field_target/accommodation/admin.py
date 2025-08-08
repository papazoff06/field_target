from django.contrib import admin

from field_target.accommodation.models import Accommodation


# Register your models here.
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    pass
