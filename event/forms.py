from django import forms
from django.forms import ModelForm

from certificate.event.models import student

class Search(ModelForm):
    model = student
    fields = ['name','email', 'mobile_no', 'uid']