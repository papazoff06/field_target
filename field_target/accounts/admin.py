from django.contrib import admin

from field_target.accounts.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ['pk', 'user', 'shooter_class', 'rifle', 'scope', 'pellets', 'country' ]
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'shooter_class']
    ordering = ('country',)
    list_filter = ['shooter_class', 'country']
    list_editable = ['shooter_class', 'rifle', 'scope', 'country', 'pellets']
