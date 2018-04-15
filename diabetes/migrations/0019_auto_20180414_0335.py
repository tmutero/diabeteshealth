# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-14 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0018_auto_20180414_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_number', models.CharField(blank=True, max_length=500)),
                ('firstname', models.CharField(blank=True, max_length=500)),
                ('lastname', models.CharField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('address', models.CharField(blank=True, max_length=500)),
                ('contact', models.CharField(blank=True, max_length=500)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnant', models.CharField(max_length=50)),
                ('glucose', models.CharField(max_length=50)),
                ('pressure', models.IntegerField(blank=True, null=True)),
                ('skin', models.IntegerField(blank=True, null=True)),
                ('insulin', models.IntegerField(blank=True, null=True)),
                ('mass', models.CharField(max_length=50)),
                ('predegree', models.CharField(max_length=5, null=True)),
                ('date_created', models.DateField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetes.Patient')),
            ],
        ),
        migrations.AlterField(
            model_name='doctors',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diabetes.Doctors'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='diabetes.Patient'),
        ),
    ]