import pytest
from model_bakery import baker

from gypz.django_assertions import assert_equal


@pytest.fixture
def user(db, django_user_model):
    user = baker.make(django_user_model, first_name='Ramiro')
    return user


def test_create_user(user):
    assert_equal(user.first_name, 'Ramiro')
