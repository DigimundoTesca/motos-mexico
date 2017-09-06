from django.contrib import admin
from .models import MotorcycleOwner


@admin.register(MotorcycleOwner)
class MotorcycleOwnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'rfc', ]
    list_display_links = ['id', 'name', ]
