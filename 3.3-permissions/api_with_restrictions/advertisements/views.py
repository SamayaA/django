from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import AdvertisementPermission
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = [AdvertisementPermission]
