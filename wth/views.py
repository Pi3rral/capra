from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from capra.views import get_graph
from wth.serializers import MeasureSerializer, LocationSerializer
from wth.models import Measure, Location
import arrow


def index(request):
    measures = Measure.objects.filter(location__name='rangement').all()

    graph_temp = get_graph(measures, 'temperature', "Temperature", 'red')
    graph_hum = get_graph(measures, 'humidity', "Humidity", 'blue')

    return render(request, 'capra/graph.html', {
        'graphs': [
            graph_temp,
            graph_hum
        ]
    })


class MeasureViewSet(viewsets.ModelViewSet):

    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer
    filter_fields = ('location__name',)

    def get_queryset(self):
        start_at = self.request.query_params.get('start_at', None)
        end_at = self.request.query_params.get('end_at', None)
        filtered_query_set = super(MeasureViewSet, self).get_queryset()
        if start_at:
            filtered_query_set = filtered_query_set.filter(
                measured_at__gt=arrow.get(start_at).datetime
            )
        if end_at:
            filtered_query_set = filtered_query_set.filter(
                measured_at__lt=arrow.get(start_at).datetime
            )
        return filtered_query_set

    def perform_create(self, serializer):
        last = Measure.objects.filter(
            location__name=serializer.validated_data['location'].name
        ).latest('measured_at')
        if not last \
                or last.temperature != \
                        serializer.validated_data['temperature'] \
                or last.humidity != \
                        serializer.validated_data['humidity']:
            serializer.save()

    def create(self, request, *args, **kwargs):
        params = self.request.query_params
        request_data = {k: v[0] for k,v in dict(params).items()}
        if request_data:
            request._full_data = request_data
        return super(MeasureViewSet, self).create(request, *args, **kwargs)


class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_fields = ('name',)
