from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.views.generic import CreateView
from django.views import View

from .models import Profile


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_invalid(self, form):
        # If the form had an error we display the error message to the user
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, error)

        return self.render_to_response(self.get_context_data(form=form))
    
    def form_valid(self, form):
        # User has successfully created a new account
        response = super().form_valid(form)
    
        # Log them into the new account
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)

        # Create a profile for the user
        Profile.objects.create(user=user)


        # Send them to the app
        if user is not None:
            login(self.request, user)
            return redirect(reverse_lazy("inbox"))
        return response


class LoginView(View):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            # User logged in successfully
            login(request, user)
            return redirect(reverse_lazy("inbox"))
        else:
            # We do not disclose which was incorrect for security reasons
            messages.error(request, "Invalid username or password.")

            return render(request, self.template_name)
