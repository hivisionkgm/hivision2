from django import forms

class feedbackforms(forms.Form):
    name=forms.CharField(max_length=40)
    email=forms.CharField(max_length=40)
    message=forms.CharField(max_length=200)

class adminforms(forms.Form):
    mail = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)