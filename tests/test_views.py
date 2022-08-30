import pytest
from django.urls import reverse


def test_home_page(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 302


@pytest.mark.django_db(transaction=True)
def test_calc_index_page(client):
    url = reverse('calc:index', kwargs={'a': 2, 'b': 3})
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db(transaction=True)
def test_history_page(client):
    url = reverse('calc:history')
    response = client.get(url)

    assert response.status_code == 200
