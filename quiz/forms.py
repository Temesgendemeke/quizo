from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationCustom(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "username",
                "placeholder": "Enter Username",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "id": "email", "placeholder": "Enter Email"}
        ),
    )
    password1 = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password1",
                "placeholder": "Enter Password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "password2",
                "placeholder": "Confirm Password",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            self.add_error("password2", "Password do not match")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "username already exists")
        if User.objects.filter(email=email).exists():
            return self.add_error("email", "email already exists")

        return cleaned_data

    def save(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        return user
