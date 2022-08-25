from django.urls import reverse


def test_home_page(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 302


def test_calc_index_page(client):
    url = reverse('calc', kwargs={'a': 2, 'b': 3})
    response = client.get(url)

    assert response.status_code == 200
