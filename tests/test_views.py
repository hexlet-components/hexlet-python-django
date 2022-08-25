from django.urls import reverse


def test_home_page(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200


def test_calc_index_page(client):
    url = reverse('calc:index')
    response = client.get(url)

    assert response.status_code == 200
