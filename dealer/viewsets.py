
from dealer.serializers import DealerSerializer, GetAcceptDealerSerializer, OfficialSerializer, PostAcceptDealerSerializer
from dealer.models import Dealer, Official, AcceptDealer
from rest_framework import viewsets


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OfficialViewSet(viewsets.ModelViewSet):
    queryset = Official.objects.all()
    serializer_class = OfficialSerializer


class AcceptDealerViewSet(viewsets.ModelViewSet):
    queryset = AcceptDealer.objects.all()
    serializer_class = GetAcceptDealerSerializer


class CreateAcceptDealerViewSet(viewsets.ModelViewSet):
    queryset = AcceptDealer.objects.all()
    serializer_class = PostAcceptDealerSerializer

