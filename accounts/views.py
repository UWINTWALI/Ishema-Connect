from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'accounts/home.html', {})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
