from django import forms
from django.contrib.auth.models import User
from chat.models import UserProfile

class RegisterUser(forms.Form):
    name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self,name, username, email, password, confirm_password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_username(self):
        username = self.username
        r = User.objects.filter(username=username)
        if r.count():
            return None
        return username

    def validate_password(self):
        password1 = self.password
        password2 = self.confirm_password
        if not password1 or not password2:
            return None
        elif password2 != password1:
            return None
        return password1

    def validate_email(self):
        email = self.email
        r = UserProfile.objects.filter(email=email)
        if r.count():
            return None
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.username,
            self.email,
            self.password
        )
        return user