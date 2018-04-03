

import  matplotlib

import  sklearn.datasets
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import dates

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import City, Doctors
from .models import Disease, Facility
from .models import Symptoms

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# methods and functions
# CRUD disease
def create_disease(request):


    disease = Disease(name=request.POST['name'], description=request.POST['description'])

    disease.save()
    return redirect('read_disease')


def read_disease(request):
    diseases = Disease.objects.all()
    context = {'diseases': diseases}
    return render(request, 'disease/list.html', context)


def edit_disease(request, id):
    diseases = Disease.objects.get(id=id)
    context = {'disease': diseases}
    return render(request, 'disease/edit.html', context)


def update_disease(request, id):
    disease = Disease.objects.get(id=id)
    disease.firstname = request.POST['firstname']
    disease.lastname = request.POST['lastname']
    disease.save()
    return redirect('/disease/')


def delete_disease(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/crud/')


# methods URL symptoms
def create_symptom(request):


    symptom = Symptoms(name=request.POST['name'], description=request.POST['description'],
                       disease_id=request.POST['disease'])

    symptom.save()
    return redirect('read_symptom')


def read_symptom(request):
    symptom = Symptoms.objects.all()
    print("=========================")
    print(symptom)
    context = {'symptom': symptom}
    return render(request, 'trainingData/list.html', context)


def edit_symptom(request, id):
    diseases = Disease.objects.get(id=id)
    context = {'disease': diseases}
    return render(request, 'trainingData/edit.html', context)


def update_symptom(request, id):
    disease = Disease.objects.get(id=id)
    disease.firstname = request.POST['firstname']
    disease.lastname = request.POST['lastname']
    disease.save()
    return redirect('/trainingData/')


def delete_symptom(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/trainingData/')


# URLS facility
def create_facility(request):


    facility = Facility(name=request.POST['name'], contact=request.POST['contact'],
                        city_id=request.POST['city'])
    print("===============================")


    facility.save()
    return redirect('read_facility')


def read_facility(request):
    facilities = Facility.objects.all()


 
    cities = City.objects.all()
    context = {'facilities': facilities,
               'cities': cities}
    return render(request, 'facility/list.html', context)


def update_facility(request, id):
    symptom = Symptoms.objects.get(id=id)
    symptom.name = request.POST['name']
    symptom.description = request.POST['description']
    symptom.save()
    return redirect('/facility/')


def delete_facility(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/facility/')

# City Panel
def create_city(request):
    city = City(name=request.POST['name'])

    city.save()
    return redirect('read_city')


def read_city(request):
    cities = City.objects.all()

    context = {'cities': cities}
    return render(request, 'city/list.html', context)


def delete_city(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/city/')


#Doctor Panel
def create_doctor(request):
    doctor = Doctors(name=request.POST['name'], surname=request.POST['surname'],
                     sex=request.POST['sex'],contact=request.POST['contact'],
                     facility_id=request.POST['facility'])

    doctor.save()
    return redirect('read_doctor')


def read_doctor(request):
    doctors = Doctors.objects.all()
    facilities = Facility.objects.all()


    context = {'doctors': doctors,
               'facilities': facilities,}
    return render(request, 'doctor/list.html', context)


def delete_doctor(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/city/')

def process(request):
#    trainingData = Symptoms(pregnant=request.POST['pregnant'],glucose=request.POST['glucose'],skin=request.POST['skin'],diastolic=request.POST['diastolic'],gender=request.POST['gender'],insulin=request.POST['insulin']
 #                           )
    current=User.objects.filter(username="tmutero")

    print(current)

    # print("___________________________________________________________________")
    # for p in Doctors.objects.raw('SELECT id ,name,sex FROM diabetes_doctors'):
    #     print("==============================")
    #     print(p)

    doctors =Doctors.objects.all()

    context = {'member': "", 'doctors': doctors, }
    template = loader.get_template('diagnosis.html')
    return HttpResponse(template.render(context, request))
