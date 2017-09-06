from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import EntryOrder, Sinister
from motorcycles.models import MotorcycleDamages, StatusTyre, StatusMotorcyclePart, MotorcyclePart
from clients.models import MotorcycleOwner


class StatusTyreInline(NestedStackedInline):
    model = StatusTyre
    extra = 2


class SinisterInline(NestedStackedInline):
    model = Sinister


class StatusMotorcyclePartInline(NestedStackedInline):
    model = StatusMotorcyclePart


class MotorcycleDamagesInline(NestedStackedInline):
    model = MotorcycleDamages
    inlines = [
        StatusMotorcyclePartInline,
        StatusTyreInline,
    ]


@admin.register(EntryOrder)
class EntryOrderAdmin(NestedModelAdmin):
    list_display = ['order', 'created_at', 'motorcycle_owner', ]
    list_display_links = ['order', 'created_at', ]
    inlines = [
        SinisterInline,
        MotorcycleDamagesInline,
    ]

admin.register(MotorcyclePart)
