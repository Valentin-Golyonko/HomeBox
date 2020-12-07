class Choices:
    DEVICE_TYPE_BAROMETER = 1
    DEVICE_TYPE_CHOICES = [
        (DEVICE_TYPE_BAROMETER, 'Barometer'),
    ]

    DEVICE_SUB_TYPE_BME280 = 1
    DEVICE_SUB_TYPE_CHOICES = [
        (DEVICE_SUB_TYPE_BME280, 'BME280'),
    ]

    DEVICE_ADDRESS_TYPE_I2C = 1
    DEVICE_ADDRESS_TYPE_ETH_WIFI = 2
    DEVICE_ADDRESS_TYPE_CHOICES = [
        (DEVICE_ADDRESS_TYPE_I2C, 'I2C'),
        (DEVICE_ADDRESS_TYPE_ETH_WIFI, 'Ethernet/WiFi')
    ]