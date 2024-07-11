import pytest 
import json
from datetime import date
from ..models import *
from Consultation.models import Doctor
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.urls import reverse,resolve
from django.test import Client

@pytest.mark.django_db
class TestGenerateToken():

    def test_generate_token_GET(self):

        host     = Client()

        response = host.get(
            path = reverse("generate_token"),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # rigth  method
        assert response.status_code == 200

    def test_generate_token_POST(self):

        host     = Client()

        response = host.post(
            path = reverse("generate_token"),
            headers={
                "Origin":"http://127.0.0.1:3000",
            },
        )

        # allowed origin
        # wrong  method
        assert response.status_code == 405

@pytest.mark.django_db
class TestLogIn():

    def setup_method(self):

        # create user
        self.user_instance = User.objects.create_user(
            username="user",
            password="password",
        )

        # create doctor
        self.doctor_instance = Doctor.objects.create(
            id =20,
            name = "Pedrou",
            last_name = "Kibutsuyi Muzan",
            birthday = date(1995,6,7),
            type_document = "passport",
            number_document = "123465789-ZW",
            phone_code = "51",
            phone_number = "951935745",
            email_address = "outlook@outlook.com",
            home_address = "Home in LA-USA",
            user_id = self.user_instance,
        )

        # add group
        group, created = Group.objects.get_or_create(name='Doctors')
        self.user_instance.groups.add(group)

    @pytest.mark.skip(reason="unexpected paremeter by django when GET")
    def test_log_in_GET(self):

        host     = Client()

        body     = json.dumps({
            "user_name": self.user_instance.username, 
            "password": "password", #no hashing
        })

        response = host.get(
            path = reverse("log_in"),
            headers={
                "Origin":"http://127.0.0.1:3000",
                "Content-Type":"application/json",
                "X-CSRFToken": "................"
            },
            content_type = "application/json",
            data= body
        )   
        
        print(response.content)

        # allowed origin
        # json format
        # csrf token
        # body data (username - password - group)
        # wrong  method
        assert response.status_code == 405

    def test_log_in_POST(self):

        host     = Client()

        body     = json.dumps({
            "user_name": self.user_instance.username, 
            "password": "password", #no hashing
        })

        response = host.post(
            path = reverse("log_in"),
            headers={
                "Origin":"http://127.0.0.1:3000",
                "Content-Type":"application/json",
                "X-CSRFToken": "................"
            },
            content_type = "application/json",
            data= body
        )   

        # allowed origin
        # json format
        # csrf token
        # body data (username - password - group)
        # rigth  method
        assert response.status_code == 200
