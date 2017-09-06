from django.db import models
from clients.models import MotorcycleOwner

class EntryOrder(models.Model):
    order = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    on_tow = models.BooleanField(default=True)
    motorcycle_owner = models.ForeignKey(MotorcycleOwner)
    # adviser  FK
    # appraiser FK

    class Meta:
        verbose_name = 'Órden de entrada'
        verbose_name_plural = 'Órdenes de entrada'

    def __str__(self):
        return '%s' % self.order


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
    is_secured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Siniestro'
        verbose_name_plural = 'Siniestros'

    def __str__(self):
        return '%s' % self.sinister
