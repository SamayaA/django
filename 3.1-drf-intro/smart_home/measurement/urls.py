from django.urls import path
from .views import SensorView, SingleSensorView,MeasurementView
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
