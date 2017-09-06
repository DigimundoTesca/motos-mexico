from django.contrib import admin
from .models import EntryOrder, MotorcyclePart, MotorcycleRegion


@admin.register(EntryOrder)
class EntryOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'created_at', 'on_tow', ]


class MotorcyclePartInline(admin.TabularInline):
    model = MotorcyclePart


@admin.register(MotorcycleRegion)
class MotorcycleRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    inlines = [
        MotorcyclePartInline,
    ]
