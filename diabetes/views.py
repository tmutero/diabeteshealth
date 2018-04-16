
import time
import  matplotlib.pyplot as plt
import pandas as pd
import  sklearn.datasets
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import dates
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from diabetes.forms import SignUpForm
from .models import City, Doctors, Profile
from .models import Disease, Facility
from .models import Symptoms,Appointment, Patient, PatientRecords

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

    request.user.id
    patient_record1 = PatientRecords.objects.get(id=precord_id)
    print("======================================================",patient_record1.pregnant)
    patient_record1.glucose
    print("-----------------------------------------------",patient_record1)


    print("--------------------------------Record Value------------------------------------------------------------",precord_id)
    print( "-=========================================--Patient----------------------------------------",id)
    patient_record=PatientRecords.objects
    data = pd.read_csv("uploads/final.csv")

# Convert categorical variable to numeric



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
    y_pred = gnb.predict(X_test[used_features])
    print(data.head())
    print ("Dataset Lenght:: ", len(data))
    print ("Dataset Shape:: ", data.shape)

   # predict=gnb.predict([[int(pregnant),int(glucose),int(pressure),int(skin),int(insulin),
        #                 float(mass),float(pedegree),int(age)]])
#   #  print(gnb.predict([[0, 3, 0, 0, 0, 34, 2, 1]]))

    #accuracy = accuracy_score(X_train, predict)
    #print(accuracy)


    patient =Patient.objects.filter(id=id)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1",patient)
    #print(predict)

    context = {'predict': "", 'patient': "patient", }
    template = loader.get_template('diagnosis.html')
    return HttpResponse(template.render(context, request))

def appointment(request, id):


    patient = Patient.objects.get(id=id)
    user= User.objects.get(id=request.user.id)
    print("==================Doctor========",patient)
    print("==================User==========",user)


    appointment= Appointment(doctor=user,patient=patient)
    #print("--------------------------------------------appointment",appointment)
    appointment.save()

    return redirect('/success/')

def read_appointment(request):

    appointments = Appointment.objects.filter().order_by('-id')

    context = {'appointments': appointments, }
    return render(request, 'report/list.html', context)

#Patient Module
def read_patient(request):
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
    patient = Patient.objects.get(id=id)
    patient.firstname = request.POST['firstname']
    patient.lastname = request.POST['lastname']
    patient.save()
    return redirect('/read_patient/')

def view_patient_record(request, id):
    #print("-------------------------",id)
    patient=Patient.objects.get(id=id)
    patient_record=PatientRecords.objects.filter(patient_id=id)

    print("============================================================")
    print(patient_record)

    contex={'patient':patient,
            'patient_record':patient_record}
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


    return

def read_user(request):
    users = User.objects.all()
    print("=========================")
    print(users)
    context = {'users': users}
    return render(request, 'user/list.html', context)

def create_user(request):

    return  0