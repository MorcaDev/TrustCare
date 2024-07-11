import pytest
from django.urls import reverse, resolve
from ..views import *

def test_patient_data():

    url = reverse("patient_data",args=["12345678"])

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == patient_data

def test_doctor_data():

    url = reverse("doctor_data")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == doctor_data

def test_new_consultation():

    url = reverse("new_consultation")

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == new_consultation

def test_patient_history():

    url = reverse("patient_history",args=["12345678"])

    url_elements = resolve(url)

    view_associated = url_elements.func

    assert view_associated == patient_history

