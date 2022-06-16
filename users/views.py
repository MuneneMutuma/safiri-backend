from users.models import Member
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import SignUpForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import MemberSerializer, MemberLoginSerializer
from django.shortcuts import redirect
from rest_framework import permissions

class MemberSignUp(APIView):
    def post(self, request):
        form = SignUpForm(request.data)
        if form.is_valid():
            form.save()
            return Response(status.HTTP_201_CREATED)
        return Response(status.HTTP_406_NOT_ACCEPTABLE)
        

class MemberView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    login_url = 'login/'
    redirect_field_name = 'member-login'
    serializer_class = MemberSerializer

    def get(self, request):
        members = Member.objects.all()
        serializer = self.serializer_class(members, many = True)
        return Response(serializer.data)

class MemberLogin(APIView):
    serializer_class = MemberLoginSerializer

    def post(self, request):
        data = request.data
        response_data = serializer_class(data=data)
        return Response(response_data)

class LoginTest(APIView):
    def post(self, request):
        print(request)

def logout_view(request):
    logout(request)
    return redirect("/bookings")