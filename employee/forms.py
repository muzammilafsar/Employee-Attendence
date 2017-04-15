from django import forms

class FilerbyDate(forms.Form):
    date=forms.DateField()