import pytest
from django.urls import reverse, resolve
from ..views import *

def test_new_email():

    # string => enpoint
    url = reverse("new_email")

    # object => enpoint , view associated, args necessary, . name, ...
    url_elements = resolve(url)

    # object => view realted
    view_associated = url_elements.func

    assert view_associated == new_email

def test_drop_email():

    url = reverse("drop_email",args=["email@provider.com"])

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == drop_email

