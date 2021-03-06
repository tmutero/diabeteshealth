from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    department=models.CharField(max_length=500, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_created=models.DateField(auto_now_add=True, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    longtitude=models.CharField(max_length=20,blank=True, null=True)
    latitude=models.CharField(max_length=20,blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.contact

class Symptoms(models.Model):
    pregnant = models.CharField(max_length=50)
    glucose = models.CharField(max_length=50)
    pressure=models.IntegerField(blank=True, null=True)
    skin=models.IntegerField(blank=True, null=True)
    insulin = models.IntegerField(blank=True, null=True)
    mass = models.CharField(max_length=50)
    predegree = models.CharField(max_length=5, null=True)
    age=models.CharField(max_length=30,blank=True, null=True)
    variable=models.BooleanField(default=False)



    def __str__(self):
        return self.pregnant + " " + self.glucose

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    date_created=models.DateField(auto_now=True)
    facility=models.ForeignKey('Facility', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name + " " + self.surname

class City(models.Model):
    name = models.CharField(max_length=50)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):

    doctor = models.ForeignKey('Doctors', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    patient = models.OneToOneField('Patient', on_delete=models.CASCADE)


    def __unicode__(self):
        return self.name


class Patient(models.Model):
    patient_number=models.CharField(max_length=500,blank=True)
    firstname=models.CharField(max_length=500, blank=True)
    lastname=models.CharField(max_length=500, blank=True)
    birth_date=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=1,blank=True)
    address=models.CharField(max_length=500, blank=True)
    contact=models.CharField(max_length=500,blank=True)
    date_created=models.DateField(auto_now=True)

    def age(self):
        import datetime
        return int((datetime.date.today() - self.birth_date).days / 365.25)

class PatientRecords(models.Model):
    pregnant = models.IntegerField(blank=True, null=True)
    glucose = models.IntegerField(blank=True, null=True)
    pressure = models.IntegerField(blank=True, null=True)
    skin = models.IntegerField(blank=True, null=True)
    insulin = models.IntegerField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    predegree = models.FloatField(blank=True, null=True)
    date_created=models.DateField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosed=models.BooleanField(default=False)
    status=models.BooleanField(default=False)

