from django import forms

class ContactUs(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.CharField(label="E-mail", max_length=100)
    topic = forms.CharField(label="Topic", max_length=100)
    message = forms.CharField(label="Message", max_length=200)