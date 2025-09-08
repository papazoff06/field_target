from django.contrib import admin

from field_target.competitions.models import Competition, Registration


# Register your models here.
@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    model = Competition
    list_display = ['name', 'start_date', 'end_date', 'location', 'description', ]


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('shooter', 'competition', 'first_day_score', 'second_day_score', 'tird_day_score', 'total_score')
    list_filter = ('competition',)
    search_fields = ('shooter__user__first_name', 'shooter__user__last_name', 'competition__name')
    readonly_fields = ('total_score',)

    def total_score(self, obj):
        return obj.total_score