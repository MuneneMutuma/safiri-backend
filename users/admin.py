from django.contrib import admin
from .models import Member
from django.contrib.auth.admin import UserAdmin
from .forms import MemberCreationForm,MemberChangeForm

# Register your models here.
class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ['username','email','phone_number','national_id','date_of_birth',]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('phone_number','national_id','date_of_birth')}),
    )
    add_fieldsets =UserAdmin.add_fieldsets + (
        (None,{'fields':('phone_number','national_id','date_of_birth')}),
    )


admin.site.register(Member,MemberAdmin)
