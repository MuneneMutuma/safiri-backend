from statistics import mode
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Member

class MemberCreationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = UserCreationForm.Meta.fields + ('date_of_birth','phone_number','national_id',)

class MemberChangeForm(UserChangeForm):
    class Meta:
        model = Member
        fields = UserChangeForm.Meta.fields    