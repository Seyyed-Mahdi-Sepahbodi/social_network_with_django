from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            User.objects.create_user(form_cleaned_data['username'], form_cleaned_data['email'], form_cleaned_data['password1'])
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            user = authenticate(request, username=form_cleaned_data['username'], password=form_cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully.', 'success')
                return redirect('home:home')
            messages.error(request, 'username or password is wrong!', 'warning')
        return render(request, self.template_name, {'form':form})