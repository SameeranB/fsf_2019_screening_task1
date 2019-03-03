from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from .forms import LoginForm
from django.views.generic.base import View
# Create your views here.



class LoginView(FormView):
    template_name = 'LoginSignup/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['Username'], password=form.cleaned_data['Password'])
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy('Home'))
        else:
            raise ValidationError("Incorrect Username or Password")
    def get_success_url(self):
        return HttpResponseRedirect(reverse_lazy('Home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LoginForm'] = LoginForm
        return context

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(LoginRequiredMixin, View):
    login_url = '/login_signup/login'
    redirect_field_name = '/home.html'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('Home'))


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Home')
    template_name = 'LoginSignup/signup.html'

