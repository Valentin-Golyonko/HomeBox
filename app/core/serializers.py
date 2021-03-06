from rest_framework import serializers

from app.core.models import Device


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'title',
            'device_type',
            'sub_type',
            'address_type',
            'i2c_address',
            'ip_address',
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=1, required=True,
        style={'input_type': 'username', 'placeholder': 'Username'},
    )
    password = serializers.CharField(
        min_length=1, required=True,
        style={'input_type': 'password', 'placeholder': 'Password'},
    )
