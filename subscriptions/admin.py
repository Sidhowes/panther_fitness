from django.contrib import admin
from .models import Programme


class Subscription_Admin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    list_display = (
        'programme_duration',
    )


admin.site.register(Programme, Subscription_Admin)