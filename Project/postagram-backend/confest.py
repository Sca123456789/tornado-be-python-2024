import pytest
from rest_framework.test import APIClient

@pytest.ficture
def client():
    return APIClient
