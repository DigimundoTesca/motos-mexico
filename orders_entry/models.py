from django.db import models


class EntryOrder(models.Model):
    order = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    on_tow = models.BooleanField(default=True)
    # adviser  FK
    # appraiser FK
    #

    class Meta:
        verbose_name = 'Órden de entrada'
        verbose_name_plural = 'Órdenes de entrada'

    def __str__(self):
        return '%s' % self.order


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


class Sinister(models.Model):
    entry_order = models.OneToOneField(
        EntryOrder,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    sinister = models.CharField(max_length=14, default='')
    insurance_carrier = models.CharField(max_length=72, default='')
    policy = models.CharField(max_length=14, default='')
    deductible = models.DecimalField(max_digits=13, decimal_places=4, default=0)
    is_secured = models.FloatField(default=False)

    class Meta:
        verbose_name = 'Siniestro'
        verbose_name_plural = 'Siniestros'

    def __str__(self):
        return '%s' % self.sinister


class Motorcycle(models.Model):
    entry_order = models.ForeignKey(EntryOrder)
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
        pass


class MotorcycleDamages(models.Model):
    entry_order = models.OneToOneField(
        EntryOrder,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    observations = models.TextField()
    
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
    

class StatusOptions(models.Model):
    status = models.CharField(max_length=3)
    
    class Meta:
        verbose_name = 'Opciones de Estado de la Moto'
        verbose_name_plural = 'Opciones de Estados de las Motos'
        
    def __str__(self):
        return '%s' % self.status
    

class StatusPart(models.Model):
    entry_order = models.ForeignKey(EntryOrder, on_delete=models.CASCADE)
    motorcycle_part = models.ForeignKey(MotorcyclePart, on_delete=models.CASCADE)
    status_option = models.ForeignKey(StatusOptions, on_delete=models.CASCADE)
