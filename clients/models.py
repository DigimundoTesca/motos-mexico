from django.db import models


class MotorcycleOwner(models.Model):
    responsible = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=75, default='')
    last_name = models.CharField(max_length=120, default='')
    address = models.CharField(max_length=120, default='')
    colony = models.CharField(max_length=120, default='')
    rfc = models.CharField(max_length=13, unique=True, blank=True, null=True)
    postal_code = models.CharField(max_length=5, default='')
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=72, default='')
    phone_1 = models.CharField(max_length=14, default='')
    phone_2 = models.CharField(max_length=14, default='')

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % self.name
