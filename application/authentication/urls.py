from django.urls import path
from .views import AuthenticationView, AuthenticationViewSet

urlpatterns = [
    path(
        "auth/",
        AuthenticationView.as_view(),
        name="auth-view"
    ),
    path(
        "auth/login/",
        AuthenticationViewSet.as_view({"post": "login"}),
        name="auth-login"
    ),
    path(
        "auth/register/",
        AuthenticationViewSet.as_view({"post": "register"}),
        name="auth-register"
    )
]