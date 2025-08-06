from django.contrib import admin

from field_target.competitions.models import Competition, Registration, Announcement


# Register your models here.
@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    model = Competition
    list_display = ['name', 'start_date', 'end_date', 'location', 'description',]

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    model = Registration

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    model = Announcement