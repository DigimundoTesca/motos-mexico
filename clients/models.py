from django.db import models


class MotorcycleOwner(models.Model):
    responsible = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120, default='')
    address = models.CharField(max_length=120, default='')
    colony = models.CharField(max_length=120, default='')
    rfc = models.CharField(max_length=13, default='')
    postal_code = models.CharField(max_length=5, default='00000')
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=72)
    phone_1 = models.CharField(max_length=14)
    phone_2 = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        pass
