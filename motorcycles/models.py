from django.db import models

from orders_entry.models import EntryOrder


class Motorcycle(models.Model):
    brand = models.CharField(max_length=45, default='')
    version = models.CharField(max_length=45, default='')
    plates = models.CharField(max_length=12, default='')
    vin = models.CharField(max_length=18, default='')
    engine_number = models.CharField(max_length=18, default='')
    model = models.CharField(max_length=4)
    sub_brand = models.CharField(max_length=18, default='')

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"

    def __str__(self):
        return '%s' % self.entry_order


class MotorcycleRegion(models.Model):
    name = models.CharField(max_length=72, default='')

    class Meta:
        verbose_name = 'Región de la Moto'
        verbose_name_plural = 'Regiones de la Moto'

    def __str__(self):
        return '%s' % self.name


class MotorcyclePart(models.Model):
    name = models.CharField(max_length=72, default='')
    motorcycle_region = models.ForeignKey(MotorcycleRegion)

    class Meta:
        verbose_name = "Parte de la Moto"
        verbose_name_plural = "Partes de la Moto"

    def __str__(self):
        return '%s' % self.name


class MotorcycleDamages(models.Model):
    entry_order = models.OneToOneField(
        EntryOrder,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    observations = models.TextField(default='Ninguna')

    class Meta:
        verbose_name = 'Daños de la moto'
        verbose_name_plural = 'Daños de las motos'

    def __str__(self):
        return '%s' % self.entry_order


class StatusTyre(models.Model):
    position = models.CharField(max_length=2)
    rim = models.CharField(max_length=1)
    lifetime = models.CharField(max_length=3)
    condition = models.TextField()
    brand = models.CharField(max_length=45)
    motorcycle_damages = models.ForeignKey(MotorcycleDamages)

    class Meta:
        verbose_name = 'Estado de la llanta'
        verbose_name_plural = 'Estado de las llantas'

    def __str__(self):
        return '%s' % self.pk


class StatusMotorcyclePart(models.Model):
    YES = 'YS'
    NO = 'NO'
    WITH_DAMAGES = 'WD'
    QUART = 'QU'
    MIDDLE = 'MI'
    ONE = 'ON'

    OPTIONS = (
    (YES, 'Sí'),
    (NO, 'No'),
    (WITH_DAMAGES, 'Con Daños'),
    (QUART, '1/4'),
    (MIDDLE, '1/2'),
    (ONE, '1/1'),
    )

    motorcycle_damages = models.ForeignKey(MotorcycleDamages)
    motorcycle_part = models.ForeignKey(MotorcyclePart, on_delete=models.CASCADE)
    status = models.CharField(choices=OPTIONS, max_length=2, default=YES)
