from users.models import Member, Msafiri
from rest_framework import serializers
from django.contrib.auth import authenticate

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username', 'phone_number', 'password', 'date_of_birth', 'national_id']

class MemberLoginSerializer(serializers.ModelSerializer):
    def validate(self, data):
        username = data['username']
        password = data['password']
        
        if username is None:
            serializers.ValidationError(
                'username required to login'
            )

        if password is None:
            serializers.ValidationError(
                'password required to login'
            )
        
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'User with this password does not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return {
            "username": username,
            "email": email
        }