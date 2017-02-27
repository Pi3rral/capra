from smb.models import Element, Temperature
from rest_framework import serializers


class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = (
            'id',
            'name',
            'temperatures',
        )


class TemperatureSerializer(serializers.ModelSerializer):
    element = serializers.SlugRelatedField(slug_field='name',
                                           queryset=Element.objects.all())

    class Meta:
        model = Temperature
        fields = (
            'id',
            'measured_at',
            'temperature',
            'element'
        )
