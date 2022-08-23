

from rest_framework import serializers

from dealer.models import Dealer, Official, AcceptDealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['rnc', 'name', 'direction', 'phone', 'email']


class OfficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Official
        fields = ['code', 'name']


class AcceptDealerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = AcceptDealer
        fields = ['dealer', 'official', 'status']
