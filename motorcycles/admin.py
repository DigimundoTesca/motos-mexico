from django.contrib import admin
from .models import MotorcyclePart, MotorcycleRegion, MotorcycleModel, \
    MotorclycleBrand, Status, StatusGroup


class MotorcyclePartInline(admin.TabularInline):
    model = MotorcyclePart


@admin.register(MotorcycleRegion)
class MotorcycleRegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    inlines = [
        MotorcyclePartInline,
    ]


@admin.register(MotorcycleModel)
class MotorcycleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', ]
    list_display_links = ['id', 'model', ]


admin.site.register(MotorcyclePart)
admin.site.register(MotorclycleBrand)
admin.site.register(Status)
admin.site.register(StatusGroup)
