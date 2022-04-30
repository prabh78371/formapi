from dataclasses import fields
from django import forms
from .models import Student

class studentform(forms.Form):
    class meta:
        model = Student
        fields = '__all__'
    