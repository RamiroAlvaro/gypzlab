import pytest
from model_bakery import baker

from gypz.card.models import Card
from gypz.django_assertions import assert_equal, assert_false


@pytest.fixture
def user(db, django_user_model):
    user = baker.make(django_user_model, first_name='Ramiro')
    return user


@pytest.fixture
def card(db, user):
    return baker.make(Card, user=user, score=299, credit=0, solicitation_status=False)


@pytest.fixture
def client_logged_user(user, client):
    client.force_login(user)
    return client


def test_create_card_score(card):
    assert_equal(card.score, 299)


def test_create_card_credit(card):
    assert_equal(card.credit, 0)


def test_create_card_solicitation_status(card):
    assert_false(card.solicitation_status)
