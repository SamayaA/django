from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters

from django.db.models import Q

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
    #Show drafts only to owner
    def get_queryset(self):
        user = self.request.user
        queryset = Advertisement.objects.filter(~Q(status='DRAFT')|
        (Q(status='DRAFT') and Q(creator__username=user)))
        return queryset
    def perform_create(self, serializer):
        #POST and PATCH methods available only for auth users
        serializer.save(creator=self.request.user)
