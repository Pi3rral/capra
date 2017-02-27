from wth.models import Measure, Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'measures'
        )


class MeasureSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(slug_field='name',
                                            queryset=Location.objects.all())

    class Meta:
        model = Measure
        fields = ('id', 'measured_at', 'temperature', 'humidity', 'location')
