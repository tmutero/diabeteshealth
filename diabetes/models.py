from django.db import models

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
    variable=models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.pregnant + " " + self.glucose

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    date_created=models.DateField()
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