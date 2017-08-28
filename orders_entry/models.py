from django.db import models


class EntryOrder(models.Model):
    order = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    on_tow = models.BooleanField(default = True)
    # adviser  FK
    # appraiser FK
    #

    class META:
        verbose_name = 'Órden de entrada'
        verbose_name_plural = 'Órdenes de entrada'

    def __str__(self):
        return '%s' % self.order
