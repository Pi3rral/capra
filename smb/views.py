from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from capra.views import get_graph
from smb.models import Temperature, Element
from smb.serializers import TemperatureSerializer, ElementSerializer


def index(request):
    elements = Element.objects.all()

    graphs = []

    for element in elements:
        measures = Temperature.objects.filter(element__name=element.name).all()
        graphs.append(get_graph(measures, 'temperature', element.name, 'red'))
        # graphs.append(get_smb_graph(element.name))

    return render(request, 'capra/graph.html', {
        'graphs': graphs
    })


class ElementViewSet(viewsets.ModelViewSet):

    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_fields = ('name',)


class TemperatureViewSet(viewsets.ModelViewSet):

    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
    filter_fields = ('element__name',)

    def perform_create(self, serializer):
        last = Temperature.objects.filter(
            element__name=serializer.validated_data['element'].name
        ).latest('measured_at')
        if not last \
                or last.temperature != serializer.validated_data['temperature']:
            serializer.save()
