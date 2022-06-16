from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Member

class SignUpForm(UserCreationForm):
    username = forms.CharField()
    phone_number = forms.IntegerField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    date_of_birth = forms.DateField()
    national_id = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    class Meta:
        model = Member
        fields = ['username', 'phone_number', 'password1', 'password2', 'date_of_birth', 'national_id', 'first_name', 'last_name', 'email']