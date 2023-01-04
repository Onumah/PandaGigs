from django.forms import ModelForm
from .models import Job
from django import forms

class JobForm(ModelForm):
    CompanyName = forms.TextInput()
    JobTitle = forms.TextInput()
    JobLocation = forms.TextInput()
    ContactEmail = forms.TextInput()
    WebsiteUrl = forms.TextInput()
    Tags = forms.TextInput()
    CompanyLogo = forms.ImageField()
    JobDescription = forms.TextInput()

    class Meta:
        model = Job
        fields = ['CompanyName', 'JobTitle', 'JobLocation', 'ContactEmail', 'WebsiteUrl', 'Tags', 'CompanyLogo', 'JobDescription']
