from django import forms

class RegUser(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField(widget = forms.EmailINput)
    password = forms.CharField(widget = forms.PasswordInput)
