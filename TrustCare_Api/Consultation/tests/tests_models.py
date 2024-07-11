import pytest 
from ..models import *
from datetime import date

"""SPECIALITY"""
@pytest.fixture
def speciality_instance():
    
    return Speciality.objects.create(
        id=100,
        name= "Cardiology"
    )

@pytest.mark.django_db
def test_speciality_attributes(speciality_instance):

    assert speciality_instance.id == 100
    assert speciality_instance.name == "Cardiology"

@pytest.mark.django_db
def test_speciality_str(speciality_instance):

    expected_result = speciality_instance.__str__()

    assert expected_result == "Cardiology"

"""DOCTOR"""
@pytest.fixture
def user_instance():

    return User.objects.create_user(
        username="User",
        password="Password"
    )

@pytest.fixture
def doctor_instance(user_instance):

    return Doctor.objects.create(
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
        user_id = user_instance,
    )

@pytest.mark.django_db
def test_doctor_attributes(doctor_instance,user_instance):

    assert doctor_instance.id   == 20
    assert doctor_instance.name  == "Pedrou"
    assert doctor_instance.last_name  == "Kibutsuyi Muzan"
    assert doctor_instance.birthday  == date(1995,6,7)
    assert doctor_instance.type_document  == "passport"
    assert doctor_instance.number_document  == "123465789-ZW"
    assert doctor_instance.phone_code  == "51"
    assert doctor_instance.phone_number  == "951935745"
    assert doctor_instance.email_address  == "outlook@outlook.com"
    assert doctor_instance.home_address  == "Home in LA-USA"
    assert doctor_instance.user_id  == user_instance

@pytest.mark.django_db
def test_doctor_str(doctor_instance):

    expected_result = doctor_instance.__str__()

    assert expected_result == "Dr. Pedrou Kibutsuyi Muzan"

"""DOCTORSPECIALITY"""
@pytest.fixture
def many_instance(doctor_instance,speciality_instance):

    return DoctorSpeciality.objects.create(
        doctor_id = doctor_instance,
        speciality_id = speciality_instance
    )

@pytest.mark.django_db
def test_many_attributes(many_instance,doctor_instance,speciality_instance):

    assert many_instance.doctor_id == doctor_instance
    assert many_instance.speciality_id == speciality_instance

@pytest.mark.django_db
def test_many_str(many_instance):

    expected_result = many_instance.__str__()

    assert expected_result == "Pedrou - Cardiology"

"""CONSULTATION"""
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

@pytest.fixture
def consultation_instance(patient_instance,doctor_instance):

    return Consultation.objects.create(
        id = 9999,
        date = date(2001,2,11),
        symptoms = "written by doctor",
        observation = "written by doctor",
        prescription = "written by doctor",
        report = "c:/pcname/dirfectory/field.ext",
        patient_id = patient_instance,
        doctor = doctor_instance,
    )

@pytest.mark.django_db
def test_consultation_attributes(consultation_instance,patient_instance,doctor_instance):
    
    assert consultation_instance.id == 9999
    assert consultation_instance.date == date(2001,2,11)
    assert consultation_instance.symptoms == "written by doctor"
    assert consultation_instance.observation == "written by doctor"
    assert consultation_instance.prescription == "written by doctor"
    assert consultation_instance.report == "c:/pcname/dirfectory/field.ext"
    assert consultation_instance.patient_id == patient_instance
    assert consultation_instance.doctor == doctor_instance

@pytest.mark.django_db
def test_consultation_str(consultation_instance):

    expected_result = consultation_instance.__str__()

    assert expected_result == "Consultation on 2001-02-11 for Jose"