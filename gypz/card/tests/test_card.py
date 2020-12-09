import pytest
from django.urls import reverse
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


@pytest.fixture
def resp(client_logged_user, db):
    return client_logged_user.get(reverse('card-list'))


def test_create_card_score(card):
    assert_equal(card.score, 299)


def test_create_card_credit(card):
    assert_equal(card.credit, 0)


def test_create_card_solicitation_status(card):
    assert_false(card.solicitation_status)


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_media_type(resp):
    assert_equal(resp.accepted_media_type, 'application/json')


@pytest.fixture
def resp_post(client_logged_user, db):
    card = {
        'id': 2,
        'user': 1,
        'score': 337,
        'credit': 1000.0,
        'solicitation_status': True,
        'solicitation_date': '2020-12-07'
    }
    return client_logged_user.post(reverse('card-list'), card)


def test_status_code_post(resp_post):
    assert_equal(resp_post.status_code, 201)


@pytest.fixture
def resp_anonymous_user(client, db):
    return client.get(reverse('card-list'))


def test_status_code_anonymous_user(resp_anonymous_user):
    assert_equal(resp_anonymous_user.status_code, 403)


@pytest.fixture
def resp_detail(client_logged_user, db, card):
    return client_logged_user.get(reverse('card-detail', kwargs={'pk': '1'}))


def test_status_code_detail(resp_detail):
    assert_equal(resp_detail.status_code, 200)


def test_content_detail(resp_detail):
    assert_equal(resp_detail.data['score'], 299)
    assert_equal(resp_detail.data['credit'], 0.0)
    assert_false(resp_detail.data['solicitation_status'])
