from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.urls import reverse
from users.forms import UserCreationForm, UserAuthenticationForm


class AuthenticationView(TemplateView):
    template_name = "auth.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["register_form"] = UserCreationForm()
        context["login_form"] = UserAuthenticationForm()
        return context


class AuthenticationViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"])
    def login(self, request):
        form = UserAuthenticationForm(request, data=request.POST)

        if not form.is_valid():
            return Response(
                {
                    "errors": form.errors,
                    "message": "Form validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                {
                    "errors": "Invalid credentials"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        login(request, user)
        return Response(
            {
                "message": "login successful",
                "redirect_url": reverse("root-view")
            },
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["post"])
    def register(self, request):
        form = UserCreationForm(data=request.POST)

        if not form.is_valid():
            return Response(
                {
                    "errors": form.errors,
                    "message": "Form validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = form.save()

        login(request, user)
        return Response(
            {
                "message": "register successful",
                "redirect_url": reverse("root-view")
            },
            status=status.HTTP_200_OK
        )
