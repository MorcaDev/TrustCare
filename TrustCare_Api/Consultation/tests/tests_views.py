import pytest 
import json
from datetime import date
from ..models import *
from Patient.models import Patient
from django.contrib.auth.models import User, Group
from django.urls import reverse,resolve
from django.test import Client

@pytest.mark.django_db
class TestPatientData():

    def setup_method(self):

        self.patient =  Patient.objects.create(
            id =10,
            name = "Jose",
            last_name = "Marchante Ikago",
            birthday = date(2001,5,22),
            type_document = "dni",
            number_document = "12345678",
            phone_code = "51",
            phone_number = "123456789",
            email_address = "email@email.com",
            home_address = "Home in bahamas 23 Mx L",
        )

    @pytest.mark.skip(reason="Login necessary")
    def test_patient_data_GET(self):

        host     = Client()

        response = host.get(
            path = reverse("patient_data", args=["12345678"]),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # url + parameters
        # rigth  method
        assert response.status_code == 200

    @pytest.mark.skip(reason="Login necessary")
    def test_patient_data_POST(self):

        host     = Client()

        response = host.post(
            path = reverse("patient_data", args=["12345678"]),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # url + parameters
        # wrong  method
        assert response.status_code == 405


@pytest.mark.django_db
class TestDoctorData():

    def setup_method(self):

        self.patient =  Patient.objects.create(
            id =10,
            name = "Jose",
            last_name = "Marchante Ikago",
            birthday = date(2001,5,22),
            type_document = "dni",
            number_document = "12345678",
            phone_code = "51",
            phone_number = "123456789",
            email_address = "email@email.com",
            home_address = "Home in bahamas 23 Mx L",
        )

    @pytest.mark.skip(reason="Login necessary")
    def test_patient_history_GET(self):

        host     = Client()

        response = host.get(
            path = reverse("patient_history", args=["12345678"]),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # url + parameters
        # rigth  method
        assert response.status_code == 200

    @pytest.mark.skip(reason="Login necessary")
    def test_patient_history_POST(self):

        host     = Client()

        response = host.post(
            path = reverse("patient_history", args=["12345678"]),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # url + parameters
        # wrong  method
        assert response.status_code == 405
