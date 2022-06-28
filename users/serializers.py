from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','phone_number','username','national_id',)
        model = Member

