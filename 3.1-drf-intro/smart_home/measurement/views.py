from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from measurement.models import Measurement, Sensor

#GET and POST methods for Sensor model
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

#GET, POST, PATCH methods for single Sensor model instance
class SingleSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

#POST method for Measurement model
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)