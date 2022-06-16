from django.urls import path
from users import views as user_views

urlpatterns = [
    path('', user_views.MemberView.as_view(), name="view-members"),
    path('create/', user_views.MemberSignUp.as_view()),
    path('login/', user_views.MemberLogin.as_view(), name="member-login"),
    path('testlogin/', user_views.LoginTest.as_view()),
    path('logout/', user_views.logout_view),
]