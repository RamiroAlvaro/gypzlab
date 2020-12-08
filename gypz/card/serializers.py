from rest_framework.serializers import ModelSerializer

from gypz.card.models import Card


class CardSerializer(ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'user', 'score', 'credit', 'solicitation_status', 'solicitation_date')
