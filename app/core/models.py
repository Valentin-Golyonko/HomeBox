from django.db import models

from app.core.core_scripts.choices import Choices


class Device(models.Model):
    title = models.CharField(
        max_length=50,
    )

    device_type = models.PositiveSmallIntegerField(
        choices=Choices.DEVICE_TYPE_CHOICES,
    )
    sub_type = models.PositiveSmallIntegerField(
        choices=Choices.DEVICE_SUB_TYPE_CHOICES,
    )

    address_type = models.PositiveSmallIntegerField(
        choices=Choices.DEVICE_ADDRESS_TYPE_CHOICES,
    )
    i2c_address = models.CharField(
        max_length=5, blank=True, null=True,
        verbose_name='I2C address',
        help_text='e.g. 0x76',
    )
    ip_address = models.GenericIPAddressField(
        blank=True, null=True,
        verbose_name='IP address',
        help_text='e.g. 192.168.0.17',
    )
    mac_address = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='MAC address',
        help_text="e.g. A1:B2:C3:D4:5E:6F",
    )
    bluetooth_uuid_tx = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='Bluetooth UUID TX',
        help_text="e.g. 0000ffe1-0000-1000-8000-00805f9b34fb",
    )
    bluetooth_uuid_rx = models.CharField(
        max_length=100, blank=True, null=True,
        verbose_name='Bluetooth UUID RX',
        help_text="e.g. 0000ffe1-0000-1000-8000-00805f9b34fb",
    )
    is_alive = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ('id',)

    def __str__(self):
        return self.title
