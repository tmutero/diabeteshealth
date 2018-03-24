

from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import scipy



from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import City
from .models import Disease, Facility
from .models import Symptoms



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# methods and functions
# CRUD disease
def create_disease(request):
    print("===============================")

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
    print("===============================")

    symptom = Symptoms(name=request.POST['name'], description=request.POST['description'],
                       disease_id=request.POST['disease'])

    symptom.save()
    return redirect('read_symptom')


def read_symptom(request):
    symptoms = Symptoms.objects.all()
    diseases = Disease.objects.all()
    context = {'symptoms': symptoms,
               'diseases': diseases}
    return render(request, 'symptom/list.html', context)


def edit_symptom(request, id):
    diseases = Disease.objects.get(id=id)
    context = {'disease': diseases}
    return render(request, 'symptom/edit.html', context)


def update_symptom(request, id):
    disease = Disease.objects.get(id=id)
    disease.firstname = request.POST['firstname']
    disease.lastname = request.POST['lastname']
    disease.save()
    return redirect('/symptom/')


def delete_symptom(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('/symptom/')


# URLS facility
def create_facility(request):
    print("===============================")

    symptom = Symptoms(name=request.POST['name'], description=request.POST['description'],
                       disease_id=request.POST['disease'])

    symptom.save()
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
    # symptom = name=request.POST['name'],description=request.POST['description'],disease_id=request.POST['disease']

    symptom=Symptoms.objects.all()



    balance_data = pd.read_csv('uploads/dataset.csv', sep=',',header=None)
    d = [balance_data]
    print("------------------------------------------",d)
    print ("Dataset Lenght:: ", len(balance_data))
    print ("Dataset Shape:: ", balance_data.shape)

    X = balance_data.values[:, 1:7]
    Y = balance_data.values[:, 8]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100,
                                      max_depth=3, min_samples_leaf=9)
    clf_gini.fit(X_train, y_train)
    DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
                           max_features=None, max_leaf_nodes=None, min_samples_leaf=9,
                           min_samples_split=2, min_weight_fraction_leaf=0.0,
                           presort=False, random_state=100, splitter='best')

    #clf_gini.predict([[6, 0, 0, 0, 0, 0]])


    y_pred = clf_gini.predict(X_test)
    y_d=clf_gini.predict(X_test,check_input=1)


    print("---------------------Result-------------------------------")
    print("......................Disease  ...............................",y_d)
    print ("Accuracy is ", accuracy_score(y_test, y_pred) * 100)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")




    print("----------------------------------------------")


    return redirect('read_disease')
