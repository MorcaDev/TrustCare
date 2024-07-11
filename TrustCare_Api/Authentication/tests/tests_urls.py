import pytest
from django.urls import reverse, resolve
from ..views import *

def test_generate_token():

    url = reverse("generate_token")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == generate_token

def test_log_in():

    url = reverse("log_in")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == log_in

def test_log_validation():

    url = reverse("log_validation")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == log_validation

def test_log_out():

    url = reverse("log_out")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == log_out
