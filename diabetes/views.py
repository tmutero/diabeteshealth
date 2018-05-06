import time
import datetime

import pandas as pd
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.template import loader

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import json

from .credentials import ACCOUNT_SID,MY_CELL,MY_TWILO,AUTH_TOKEN


from diabetes.forms import SignUpForm
from .models import City, Doctors
from .models import Disease, Facility
from .models import Symptoms, Appointment, Patient, PatientRecords

from django.http import HttpResponse
from twilio.rest import Client



def signup(request):
    if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.birth_date = form.cleaned_data.get('birth_date')
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# methods and functions
# CRUD disease
def create_disease(request):
    if not request.user.is_authenticated:
        return redirect('home')
    disease = Disease(name=request.POST['name'], description=request.POST['description'])

    disease.save()
    return redirect('read_disease')


def read_disease(request):
    if not request.user.is_authenticated:
        return redirect('home')
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
    if not request.user.is_authenticated:
        return redirect('home')
    symptom = Symptoms.objects.all()
    print("=========================")
    print(symptom)
    context = {'symptom': symptom}


    print(create_user)
    return render(request, 'trainingData/list.html', context)


def edit_symptom(request, id):
    diseases = Disease.objects.get(id=id)
    context = {'disease': diseases}
    return render(request, 'trainingData/edit.html', context)


def update_symptom(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    disease = Disease.objects.get(id=id)
    disease.firstname = request.POST['firstname']
    disease.lastname = request.POST['lastname']
    disease.save()
    return redirect('/trainingData/')


def delete_symptom(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/trainingData/')


# URLS facility
def create_facility(request):
    if not request.user.is_authenticated:
        return redirect('home')
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
    if not request.user.is_authenticated:
        return redirect('home')
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

def process(request,  precord_id,id):
    # trainingData = Symptoms(pregnant=request.POST['pregnant'],
    #                         glucose=request.POST['glucose'],
    #                         skin=request.POST['skin'],
    #                         diastolic=request.POST['diastolic'],
    #                         gender=request.POST['gender'],insulin=request.POST['insulin']
    #                )

    # pregnant = request.POST['pregnant']
    # glucose = request.POST['glucose']
    # mass = request.POST['mass']
    # skin = request.POST['skin']
    # pedegree = request.POST['pedegree']
    # pressure = request.POST['pressure']
    # insulin = request.POST['insulin']
    # age = request.POST['age']
    # print("========================Data Set================================")
    # print("----------Pregnanct",int(pregnant))
    # print("-----------age",age)
    # print("----------Pedegree",pedegree)
    # print("----------Insulin",insulin)
    # print("----------Pressure",pressure)
    # print("----------Skin",skin)
    # print("----------MAss",mass)
    # print("----------Glucose",glucose)
    # print("________________________End Of Data Set ________________________")
    if not request.user.is_authenticated:
        return redirect('home')

    current_user=request.user.id
    patient = Patient.objects.get(id=id)
    patient_record1 = PatientRecords.objects.get(id=precord_id)

    print("--------------------------------Record Value------------------------------------------------------------",precord_id)
    print( "-=========================================--Patient----------------------------------------",id)

    print("======================================================",patient_record1.pregnant)
    glucose=patient_record1.glucose
    pregnant=patient_record1.pregnant
    insulin=patient_record1.insulin
    mass=patient_record1.mass
    skin=patient_record1.skin
    pressure=patient_record1.pressure
    predegree=int(patient_record1.predegree)
    age=patient.age()

    print("-----------------------------------------------",patient_record1)
    print("-----------",age)
    print("========================Data Set================================")
    print("----------Pregnanct", int(pregnant))
    print("-----------age", age)
    print("----------Pedegree", predegree)
    print("----------Insulin", insulin)
    print("----------Pressure", pressure)
    print("----------Skin", skin)
    print("----------MAss", mass)
    print("----------Glucose", glucose)
    print("________________________End Of Data Set ________________________")

    print("--------------------------------Record Value------------------------------------------------------------",precord_id)
    print( "-=========================================--Patient----------------------------------------",id)


    data = pd.read_csv("uploads/final.csv")

# Convert categorical variable to numeric


#Algo
# Cleaning dataset of NaN
    data=data[[
    "pregnant",
    "glucose",
    "pressure",
    "skin",
    "insulin",
    "mass",
    "pedegree",
    "age",
    "class"


    ]].dropna(axis=0, how='any')

# Split dataset in training and test datasets
    X_train, X_test = train_test_split(data, test_size=0.5, random_state=int(time.time()))
    gnb = GaussianNB()
    used_features =[
    "pregnant",
    "glucose",
    "pressure",
    "skin",
    "insulin",
    "mass",
    "pedegree",
    "age",


    ]
    gnb.fit(
    X_train[used_features].values,
    X_train["class"]
    )
   # y_pred = gnb.predict(X_test[used_features])
    print(data.head())
    print ("Dataset Lenght:: ", len(data))
    print ("Dataset Shape:: ", data.shape)

    predict=gnb.predict([[pregnant,glucose,pressure,skin,insulin,
                    mass,predegree,age]])


    if predict ==1:
        print("Yes Yu are Diabetic")


        PatientRecords.objects.filter(Q(patient=id)& Q(id=precord_id)).update(diagnosed=True)
        # Send Message To Patient
        now = datetime.datetime.now()
        now = now.strftime('%d/%m/%Y')
        user = User.objects.get(id=request.user.id)

        doctor=user.get_full_name()

        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body="Dear Patient-"+patient.firstname+" "+patient.lastname+" your test for Diabetic are negative please "
                                                                        "visit hospital for assistance. "
                                                                        "Doctor Diagnosed:"+""+doctor+""+""+
                                                                        "Date Diagnosed:"+" "+now,
            to="+263774226217",
            from_="+14252875226",)

    context = {'predict': predict, 'patient': patient, }
    template = loader.get_template('diagnosis.html')
    return HttpResponse(template.render(context, request))

def appointment(request, id):

    if not request.user.is_authenticated:
        return redirect('home')

    patient = Patient.objects.get(id=id)
    user= User.objects.get(id=request.user.id)



    appointment= Appointment(doctor=user,patient=patient)

    appointment.save()

    return redirect('/success/')

def read_appointment(request):

    appointments = Appointment.objects.filter().order_by('-id')


    context = {'appointments': appointments, }
    return render(request, 'report/list.html', context)

#Patient Module
def read_patient(request):
    if not request.user.is_authenticated:
        return redirect('home')
    patients = Patient.objects.all()
    print("=========================")
    print(patients)
    context = {'patients': patients}
    return render(request, 'patient/list.html', context)


def edit_patient(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'patient/edit.html', context)


def update_patient(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    patient = Patient.objects.get(id=id)
    patient.firstname = request.POST['firstname']
    patient.lastname = request.POST['lastname']
    patient.save()
    return redirect('/read_patient/')

def view_patient_record(request, id):
    #print("-------------------------",id)
    if not request.user.is_authenticated:
        return redirect('home')
    patient=Patient.objects.get(id=id)

    diagnosis = PatientRecords.objects.filter(patient_id=id)
    patient_record=PatientRecords.objects.filter(patient_id=id)

    print("============================================================",diagnosis)
    print(patient_record)

    contex={'patient':patient,
            'patient_record':patient_record,
            'diagnosed':diagnosis,}
    return render(request,'patient/view.html',contex)

def create_patient(request):


    patient = Patient(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                       contact=request.POST['contact'],address=request.POST['address'],
                      gender=request.POST['gender'],birth_date=request.POST['birth_date'])

    patient.save()
    return redirect('read_patient')

def create_patient_clinical(request):
    patient_id=request.POST.get('patient_id')

    patient_record=PatientRecords(pregnant = request.POST.get('pregnant'),
    glucose = request.POST.get('glucose'),
    mass = request.POST.get('mass'),
    skin = request.POST.get('skin'),
    predegree = request.POST.get('pedegree'),
    pressure = request.POST.get('pressure'),
    insulin = request.POST.get('insulin'),patient_id=patient_id
                                  )
    print("========================================================",patient_record)
    patient_record.save()


    return redirect('view_patient_record',patient_id)

def read_user(request):
    if not request.user.is_authenticated:
        return redirect('home')
    users = User.objects.all()
    print("=========================")
    print(users)
    context = {'users': users}
    return render(request, 'user/list.html', context)

def report(request):
    dataset = Symptoms.objects \
        .values('variable') \
        .annotate(variable_count=Count('variable', filter=Q(variable=True)),
                  not_variable_count=Count('variable', filter=Q(variable=False))) \
        .order_by('variable')


    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Diabetic' % entry['variable'])
        survived_series_data.append(entry['variable_count'])
        not_survived_series_data.append(entry['not_variable_count'])

    not_survived_series = {
        'name': 'Diabetic Patients',
        'data': not_survived_series_data,
        'color': 'red'
    }

    survived_series = {
    'name': 'Health Patients',
    'data': survived_series_data,
    'color': 'green'
    }



    chart = {
    'chart': {'type': 'bar'},
    'title': {'text': 'Patients Distribution by diabetes'},
    'xAxis': {'categories': categories},
    'series': [survived_series, not_survived_series]
    }

    dump = json.dumps(chart)

    return render(request, 'report/list.html', {'chart': dump})

def create_user(request):
    return

def diagnosed(request):
    if not request.user.is_authenticated:
        return redirect('home')

    patient_clinicals=PatientRecords.objects.filter(diagnosed=1)


    context = {'patient_clinicals': patient_clinicals}
    return render(request, 'report/diagnosed.html', context)