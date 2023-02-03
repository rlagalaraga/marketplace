from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


class RegisterView(TemplateView):
    template_name = "users/register.html"

    def get(self, *args, **kwargs):
        return render(self.request, "users/register.html")


class LoginView(TemplateView):
    template_name = "users/login.html"

    def get(self, *args, **kwargs):
        return render(self.request, "users/login.html")


class UpdateView(TemplateView):
    template_name = "users/update-profile.html"

    def get(self, *args, **kwargs):
        return render(self.request, "users/update-profile.html")


class ProfileView(TemplateView):
    template_name = "users/profile.html"

    def get(self, *args, **kwargs):
        return render(self.request, "users/profile.html")


def LogoutView(request):

    logout(request)
    messages.success(request, 'Account Logged Out!')
    return redirect('market:dashboard')

