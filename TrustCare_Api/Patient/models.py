from django.db import models
from django.contrib.auth.models import User

# PATIENTS - CLIENTS
class Patient(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    type_document = models.CharField(max_length=10,blank=False, null=False, choices=[("dni","dni"),("passsport","passport")])
    number_document = models.CharField(max_length=12,blank=False, null=False, unique=True)
    phone_code = models.IntegerField()
    phone_number = models.IntegerField(blank=False, null=False, unique=True)
    email_address = models.EmailField(max_length=45,blank=False, null=False,unique=True)
    home_address = models.CharField(max_length=45,blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.name} {self.last_name} - {self.number_document}'

# EMPLOYEES - ASISTANT ->  GROUP
class Assistant(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    type_document = models.CharField(max_length=10,blank=False, null=False, choices=[("dni","dni"),("passsport","passport")])
    number_document = models.CharField(max_length=12,blank=False, null=False, unique=True)
    phone_code = models.IntegerField(blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False, unique=True)
    email_address = models.EmailField(max_length=45,blank=False, null=False,unique=True)
    home_address = models.CharField(max_length=45,blank=False, null=False, unique=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,blank=False, null=False,unique=True)

    def __str__(self):
        return f'{self.name} {self.last_name} - {self.number_document}'
