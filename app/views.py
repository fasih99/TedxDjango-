from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import User
from django.urls import reverse_lazy


# Create your views here.

class home(TemplateView):
    template_name = 'app/index.html'

class team(TemplateView):
    template_name = 'app/team.html'

class contactUs(TemplateView):
    template_name = 'app/contactUs.html'


class SignupView(CreateView):
    template_name = "registration/signUp.html"
    form_class = User

    def get_success_url(self):
        return reverse_lazy("login")
