from django.db import models

from orders_entry.models import EntryOrder


class MotorclycleBrand(models.Model):
    brand = models.CharField(max_length=48, default='', unique=True)

    class Meta:
        verbose_name = "Marca de la Moto"
        verbose_name_plural = "Marcas de Motos"

    def __str__(self):
        return '%s' % self.brand


class MotorcycleModel(models.Model):
    model = models.CharField(max_length=92, default='', unique=True)
    brand = models.ForeignKey(MotorclycleBrand)

    class Meta:
        verbose_name = "Modelo de Moto"
        verbose_name_plural = "Modelos de Motos"

    def __str__(self):
        return '%s' % self.model


class MotorcycleClient(models.Model):
    model = models.ForeignKey(MotorcycleModel)
    version = models.CharField(max_length=45, default='')
    plates = models.CharField(max_length=12, default='')
    vin = models.CharField(max_length=18, default='')
    engine_number = models.CharField(max_length=18, default='')
    year = models.CharField(max_length=4, default='2000')

    class Meta:
        verbose_name = "Moto"
        verbose_name_plural = "Motos"

    def __str__(self):
        return '%s' % self.entry_order

    def model(self):
        return '%s - %s' % (self.model.brand, self.model)


class MotorcycleRegion(models.Model):
    name = models.CharField(max_length=72, default='')

    class Meta:
        verbose_name = 'Región de la Moto'
        verbose_name_plural = 'Regiones de la Moto'

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
    QUART = 'Q'
    MIDDLE = 'M'
    ENTIRE = 'E'

    LIFETIME_CONDITION = (
        (QUART, '1/4'),
        (MIDDLE, '1/2'),
        (ENTIRE, '1/1'),
    )

    RIM_OPTION = (
        ('A', 'A'),
        ('R', 'R'),
    )
    position = models.CharField(max_length=2)
    rim = models.CharField(choices=RIM_OPTION, default='A', max_length=1)
    lifetime = models.CharField(choices=LIFETIME_CONDITION, default=ENTIRE, max_length=1)
    condition = models.TextField()
    brand = models.CharField(max_length=45)
    motorcycle_damages = models.ForeignKey(MotorcycleDamages)

    class Meta:
        verbose_name = 'Estado de la llanta'
        verbose_name_plural = 'Estado de las llantas'

    def __str__(self):
        return '%s' % self.pk


class StatusGroup(models.Model):
    alias = models.CharField(max_length=24, default='')

    class Meta:
        verbose_name = 'Grupo de Condiciones'
        verbose_name_plural = 'Grupos de Condiciones'

    def __str__(self):
        return '%s' % self.alias


class Status(models.Model):
    status = models.CharField(max_length=12)
    group = models.ForeignKey(StatusGroup)

    class Meta:
        verbose_name = 'Condición'
        verbose_name_plural = 'Condiciones'

    def __str__(self):
        return '%s' % self.status


class MotorcyclePart(models.Model):
    name = models.CharField(max_length=72, default='')
    motorcycle_region = models.ForeignKey(MotorcycleRegion)
    status_group = models.ForeignKey(StatusGroup)

    class Meta:
        verbose_name = "Parte de la Moto"
        verbose_name_plural = "Partes de la Moto"

    def __str__(self):
        return '%s' % self.name


class StatusMotorcyclePart(models.Model):
    motorcycle_damages = models.ForeignKey(MotorcycleDamages)
    motorcycle_part = models.ForeignKey(MotorcyclePart, on_delete=models.CASCADE)
    status = models.ForeignKey(Status)

    class Meta:
        verbose_name = 'Estado de Pieza'
        verbose_name_plural = 'Estado de las llantas'

    def __str__(self):
        return '%s' % self.pk
