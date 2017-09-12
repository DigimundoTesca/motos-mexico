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


@admin.register(MotorcyclePart)
class MotorcyclePartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'motorcycle_region', 'status_group', )
    list_display_links = ('id', 'motorcycle_region', )
    list_editable = ('status_group', 'name')
    ordering = ('motorcycle_region', 'name')

admin.site.register(MotorclycleBrand)
admin.site.register(Status)
admin.site.register(StatusGroup)
