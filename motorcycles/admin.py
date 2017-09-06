from django.contrib import admin
from .models import MotorcyclePart, MotorcycleRegion


class MotorcyclePartInline(admin.TabularInline):
    model = MotorcyclePart


@admin.register(MotorcycleRegion)
class MotorcycleRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    inlines = [
        MotorcyclePartInline,
    ]


admin.site.register(MotorcyclePart)
