import pytest 
from ..models import Patient,Assistant,User
from datetime import date

"""PATIENTS"""
@pytest.fixture
def patient_instance():

    return Patient.objects.create(
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

@pytest.mark.django_db
def test_patient_attributes(patient_instance):

    assert patient_instance.id  == 10
    assert patient_instance.name  == "Jose"
    assert patient_instance.last_name  == "Marchante Ikago"
    assert patient_instance.birthday  == date(2001,5,22)
    assert patient_instance.type_document  == "dni"
    assert patient_instance.number_document  == "12345678"
    assert patient_instance.phone_code  == "51"
    assert patient_instance.phone_number  == "123456789"
    assert patient_instance.email_address  == "email@email.com"
    assert patient_instance.home_address  == "Home in bahamas 23 Mx L"

@pytest.mark.django_db
def test_patient_str(patient_instance):

    expected_result = patient_instance.__str__()

    assert expected_result == "Jose Marchante Ikago - 12345678"

"""ASSISTANT"""
@pytest.fixture
def user_instance():

    return User.objects.create_user(
        username="User",
        password="Password"
    )

@pytest.fixture
def assistant_instance(user_instance):

    return Assistant.objects.create(
        id =20,
        name = "Diego",
        last_name = "Ichikaga Itadori",
        birthday = date(2001,5,22),
        type_document = "dni",
        number_document = "87654321",
        phone_code = "51",
        phone_number = "987654321",
        email_address = "hotemail@hotemail.com",
        home_address = "Apartment in USA - NY",
        user_id = user_instance
    )

@pytest.mark.django_db
def test_assistant_attributes(assistant_instance,user_instance):

    assert assistant_instance.id             == 20
    assert assistant_instance.name           == "Diego"
    assert assistant_instance.last_name      == "Ichikaga Itadori"
    assert assistant_instance.birthday       == date(2001,5,22)
    assert assistant_instance.type_document  == "dni"
    assert assistant_instance.number_document== "87654321"
    assert assistant_instance.phone_code     == "51"
    assert assistant_instance.phone_number   == "987654321"
    assert assistant_instance.email_address  == "hotemail@hotemail.com"
    assert assistant_instance.home_address   == "Apartment in USA - NY"
    assert assistant_instance.user_id        == user_instance

@pytest.mark.django_db
def test_assistant_str(assistant_instance):

    expected_result = assistant_instance.__str__()

    assert expected_result == "Diego Ichikaga Itadori - 87654321"