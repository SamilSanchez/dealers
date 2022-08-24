

from rest_framework import serializers

from dealer.models import Dealer, Official, AcceptDealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ['id', 'rnc', 'name', 'direction', 'phone', 'email']


class OfficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Official
        fields = ['id', 'code', 'name']


class GetAcceptDealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcceptDealer
        fields = ['id', 'dealer', 'official', 'status']
        depth = 1


class PostAcceptDealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AcceptDealer
        fields = ['id', 'dealer', 'official', 'status']
