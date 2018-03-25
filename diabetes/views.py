
import  scipy
import  pydotplus
from  sklearn.datasets import load_iris



from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import City
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
                        city=request.POST['city'])
    print("===============================")
    print(city=request.POST['city'])

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


#
def process(request):
    # trainingData = name=request.POST['name'],description=request.POST['description'],disease_id=request.POST['disease']

    symptom =Symptoms.objects.all()

    binary = pd.read_csv('http://dni-institute.in/blogs/wp-content/uploads/2017/07/dt_data.csv')
    print(binary.describe())



    return redirect('read_disease')
