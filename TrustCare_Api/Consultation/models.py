from django.db import models
from Patient.models import Patient
from django.contrib.auth.models import User

# SPECIALITIES
class Speciality(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    name = models.CharField(max_length=45,blank=False, null=False,unique=True)

    def __str__(self):
        return f"{self.name}"

# DOCTORS
class Doctor(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    collegiate_code = models.CharField(max_length=45,blank=False, null=False,unique=True)
    name = models.CharField(max_length=45,blank=False, null=False)
    last_name = models.CharField(max_length=45,blank=False, null=False)
    birthday = models.DateField(blank=False, null=False)
    type_document = models.CharField(max_length=45,blank=False, null=False,choices=[("dni","dni"),("passsport","passport")])
    number_document = models.CharField(max_length=12,blank=False, null=False)
    phone_code = models.IntegerField(blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False,unique=True)
    email_address = models.CharField(max_length=45,blank=False, null=False,unique=True)
    home_address = models.CharField(max_length=45,blank=False, null=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,blank=False, null=False,unique=True) 
    many = models.ManyToManyField(Speciality, through='DoctorSpeciality')

    def __str__(self):
        return f"Dr. {self.name} {self.last_name}"

# MANY TO MANY
class DoctorSpeciality(models.Model):

    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,blank=False, null=False)
    speciality_id = models.ForeignKey(Speciality, on_delete=models.CASCADE,blank=False, null=False)

    class Meta:
        unique_together = ('doctor_id', 'speciality_id')

    def __str__(self):
        return f"{self.doctor_id.name} - {self.speciality_id.name}"

# CONSULTATION - HISTORY
class Consultation(models.Model):

    id = models.AutoField(primary_key=True,blank=False, null=False, unique=True)
    date = models.DateField(blank=False, null=False)
    symptoms = models.TextField(blank=False, null=False)
    observation = models.TextField(blank=False, null=False)
    prescription = models.TextField(blank=False, null=False)
    report = models.FileField(upload_to="reports/",blank=True,null=True)  
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consultation on {self.date} for {self.patient_id.name}"
