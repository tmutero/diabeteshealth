"""diabeteshealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from diabetes import  views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

    #urls CRUD diseases

    url(r'^create_disease$', views.create_disease, name='create_disease'),
    url(r'^read_disease$',views.read_disease, name='read_disease'),
    url(r'^edit_disease/(?P<id>\d+)$', views.edit_disease, name='edit_disease'),
    url(r'^edit/update_disease/(?P<id>\d+)$', views.update_disease, name='update_disease'),
    url(r'^delete_disease/(?P<id>\d+)$', views.delete_disease, name='delete_disease'),

  # urls CRUD symptoms
    url(r'^create_symptom$', views.create_symptom, name='create_symptom'),
    url(r'^read_symptom$', views.read_symptom, name='read_symptom'),
    url(r'^edit_symptom/(?P<id>\d+)$', views.edit_symptom, name='edit_symptom'),
    url(r'^edit/update_symptom/(?P<id>\d+)$', views.update_symptom, name='update_symptom'),
    url(r'^delete_symptom/(?P<id>\d+)$', views.delete_symptom, name='delete_symptom'),

#urls  CRUD facilities
    url(r'^create_facility$', views.create_facility, name='create_facility'),
    url(r'^read_facility$', views.read_facility, name='read_facility'),
    url(r'^edit_facility/(?P<id>\d+)$', views.read_facility, name='edit_facility'),
    url(r'^edit/update_facility/(?P<id>\d+)$', views.update_facility, name='update_facility'),
    url(r'^delete_facility/(?P<id>\d+)$', views.delete_facility, name='delete_facility'),


    # urls CRUD City
    url(r'^create_city$', views.create_city, name='create_city'),
    url(r'^read_city$', views.read_city, name='read_city'),
  #  url(r'^edit_city/(?P<id>\d+)$', views.edit_city, name='edit_city'),
   # url(r'^edit/update_city/(?P<id>\d+)$', views.update_city, name='update_city'),
    url(r'^delete_city/(?P<id>\d+)$', views.delete_city, name='delete_city'),

    # urls CRUD doctor
    url(r'^create_doctor$', views.create_doctor, name='create_doctor'),
    url(r'^read_doctor$', views.read_doctor, name='read_doctor'),
    url(r'^delete_doctor(?P<id>\d+)$', views.delete_doctor, name='delete_doctor'),



    url(r'^process/(?P<precord_id>\d+)/(?P<id>\d)/$', views.process, name='process'),
    url(r'^appointment(?P<id>\d+)$', views.appointment, name='appointment'),
    url(r'^read_appointment$',views.read_appointment, name='read_appointment'),


    #Patients
#patients details
    url(r'^create_patient$', views.create_patient, name='create_patient'),
    url(r'^read_patient$', views.read_patient, name='read_patient'),
    url(r'^edit_patient/(?P<id>\d+)$', views.edit_patient, name='edit_patient'),
    url(r'^edit/update_patient/(?P<id>\d+)$', views.update_patient, name='update_patient'),
    url(r'^view_patient_record(?P<id>\d+)$', views.view_patient_record, name='view_patient_record'),
    #url(r'^create_patient_clinical(?P<id>\d+)$', views.create_patient_clinical, name='create_patient_clinical')
    url(r'^create_patient_clinical$', views.create_patient_clinical, name='create_patient_clinical'),


    #view users
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^read_user$', views.read_user, name='read_user'),
    url(r'^report$', views.report, name='report'),
    url(r'^diagnosed$', views.diagnosed, name='diagnosed')

]
