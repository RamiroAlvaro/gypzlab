from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gypz.card.models import Card
from gypz.card.serializers import CardSerializer
from gypz.core.serializers import UserSerializer
from random import randint


def get_credit(salary):
    score = randint(1, 999)
    credit = salary / 2 if salary / 2 > 1000 else 1000
    value = {'solicitation_status': False, 'score': 1, 'credit': 0}
    dtc_card = {
        299: {'solicitation_status': False, 'score': score, 'credit': 0},
        599: {'solicitation_status': True, 'score': score, 'credit': 1_000},
        799: {'solicitation_status': True, 'score': score, 'credit': credit},
        950: {'solicitation_status': True, 'score': score, 'credit': salary * 2},
        999: {'solicitation_status': True, 'score': score, 'credit': 1_000_000},
    }

    for upper_bound, value in dtc_card.items():
        if score <= upper_bound:
            break
    return value


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        salary = UserSerializer(request.user).data['salary']
        card = Card.objects.create(**get_credit(salary), user=request.user)
        serializer = CardSerializer(card)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
