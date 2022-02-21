from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class RegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_cleaned_data = form.cleaned_data
            User.objects.create_user(form_cleaned_data['username'], form_cleaned_data['email'], form_cleaned_data['password'])
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})