from django.db import models


class Barometer(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    pressure_pha = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = 'Barometer'
        verbose_name_plural = 'Barometer'