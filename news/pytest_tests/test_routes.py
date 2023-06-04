# YaNews Pytest Routes
import pytest

from http import HTTPStatus

from django.urls import reverse


def test_pages_availability_for_anonymous_user(client, name):
    url = reverse(name)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK