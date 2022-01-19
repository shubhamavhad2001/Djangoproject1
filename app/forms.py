from django import forms
# from django.forms.fields import CharField

class input(forms.Form):
    name=forms.CharField(max_length=300)
    id=forms.IntegerField() 