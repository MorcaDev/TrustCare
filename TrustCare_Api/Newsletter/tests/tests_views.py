import pytest 
import json
from ..models import NewsLetterEmail
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
class TestNewEmail():

    def test_new_email_GET(self):

        host     = Client()

        body     = json.dumps({"new_email":"otrorandom@proveedor.com"})

        response = host.post(
            path    = reverse("new_email"),
            headers = {
                "Origin":"http://127.0.0.1:3000",
                "Content-Type": "application/json",
                "X-CSRFToken": ".................",
            }, 
            content_type='application/json',
            data    = body,
        )


        # allowed origin
        # json format
        # email in body
        # not allowed method
        assert response.status_code == 405

    def test_new_email_POST(self):

        host     = Client()

        body     = json.dumps({"new_email":"otrorandom@proveedor.com"})

        response = host.post(
            path    = reverse("new_email"),
            headers = {
                "Origin":"http://127.0.0.1:3000",
                "Content-Type": "application/json",
                "X-CSRFToken": ".................",
            }, 
            content_type='application/json',
            data    = body,
        )

        # allowed origin
        # json format
        # email in body
        # allowed method
        assert response.status_code == 200

@pytest.mark.django_db
class TestDropEmail():
     
    def setup_method(self):

        self.new_email = NewsLetterEmail.objects.create(
            id=100,
            email="random@proveedor.com",
        )

    def test_drop_email_GET(self):

        host     = Client()

        response = host.get(
            path = reverse("drop_email", args=[self.new_email.__str__()]),
            headers={
                "Origin":"http://127.0.0.1:3000",
                "X-CSRFToken": ".................",
            },
        )

        # allowed  origin
        # csrf-token 
        assert response.status_code == 200
        
    def test_drop_email_POST(self):

        host     = Client()

        response = host.get(
            path = reverse("drop_email", args=[self.new_email.__str__()]),
            headers={
                "Origin":"http://127.0.0.1:3000",
                "X-CSRFToken": ".................",
            },
        )

        # allopwed origin
        # csrf token
        # not allowed method
        assert response.status_code == 405
