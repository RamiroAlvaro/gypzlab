import pytest
from django.urls import reverse
from model_bakery import baker

from gypz.django_assertions import assert_equal


@pytest.fixture
def user(db, django_user_model):
    user = baker.make(django_user_model, first_name='Ramiro')
    return user


@pytest.fixture
def client_logged_user(user, client):
    client.force_login(user)
    return client


@pytest.fixture
def resp(client_logged_user, db):
    return client_logged_user.get(reverse('user-list'))


def test_create_user(user):
    assert_equal(user.first_name, 'Ramiro')


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_media_type(resp):
    assert_equal(resp.accepted_media_type, 'application/json')


@pytest.fixture
def resp_post(client, db):
    user = {
        'id': 1,
        'first_name': 'ramiro',
        'last_name': 'alvaro',
        'email': 'ramiroalvaro.ra@gmail.com',
        'cpf': '700.673.051-13',
        'phone': '31991387178',
        'salary': 10000.0,
        'birthdate': '1975-11-29'
    }
    return client.post(reverse('user-list'), user)


def test_status_code_post(resp_post):
    assert_equal(resp_post.status_code, 201)
