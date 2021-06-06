from rest_framework import status
from rest_framework.reverse import reverse

from ..factories.community import CommunityFactory
from ..factories.economy import EconomyFactory
from ..factories.network import NetworkFactory


def test_community_analytics_list(api_client, django_assert_max_num_queries):
    CommunityFactory.create_batch(5)
    with django_assert_max_num_queries(7):
        r = api_client.get(reverse('community-list'), {'limit': 0})
    assert r.status_code == status.HTTP_200_OK
    assert len(r.data) == 5


def test_economy_analytics_list(api_client, django_assert_max_num_queries):
    EconomyFactory.create_batch(5)
    with django_assert_max_num_queries(7):
        r = api_client.get(reverse('economy-list'), {'limit': 0})
    assert r.status_code == status.HTTP_200_OK
    assert len(r.data) == 5


def test_network_analytics_list(api_client, django_assert_max_num_queries):
    NetworkFactory.create_batch(5)
    with django_assert_max_num_queries(7):
        r = api_client.get(reverse('network-list'), {'limit': 0})
    assert r.status_code == status.HTTP_200_OK
    assert len(r.data) == 5
