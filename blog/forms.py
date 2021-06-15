from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.exceptions import FieldDoesNotExist
from .models import Contact, Comments, Specialization, Doctor, Reception
from django.contrib.admin import widgets

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    copy = forms.BooleanField(required=False)
    
    class Meta:
	    model = Contact        

class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('specialization', 'doctor', 'date', 'time', 'patient_name', 'patient_info')

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()
        self.fields['specialization'].widget = forms.HiddenInput()
        self.fields['doctor'].widget = forms.HiddenInput()
        self.fields['patient_info'].widget = forms.Textarea(attrs={'cols': 60, 'rows': 8})
        self.fields['patient_info'].label = 'Что вас беспокоит'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('email', 'body')