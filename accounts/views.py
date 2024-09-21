from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, UserProfileForm, LoginForm, UserInfoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .models import UserProfile


def user_info(request):
    if request.user.is_authenticated:
      #find profile whose user id is [user ID]
      current_user = UserProfile.objects.get(user__id = request.user.id)
      form = UserInfoForm(request.POST or None, instance = current_user)
      
      if form.is_valid():
        form.save()
        messages.success(request, ("Profile Info Updated Successfully!!"))
        return redirect('accounts:user_info')
      return render(request, 'accounts/user_info.html', {'form': form })
    else:
      messages.success(request, ("You must be logged in to view that page"))
      return redirect('accounts:welcome')
    





def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('community:home')  # Redirect to home or another page after login
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})





def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('accounts:welcome')  # Redirect to home or another page after logout
    else:
        return redirect('accounts:welcome')  # Redirect to home or another page if not POST request


def welcome(request):
    context = {
        'range': range(3)
    }
    return render(request, 'accounts/welcome.html', context)


def register(request):
    user_form = SignUpForm()
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create and save the user
            user_form.save()

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            
            # Authenticate the user
            user = authenticate(username=username, password=password)
            
            # Check if authentication was successful
            if user is not None:
                # Log in the user
                auth_login(request, user)
                messages.success(request, "Fill out the personal info section")
                return redirect('accounts:user_info')
            else:
                messages.error(request, "There was a problem logging in after registration.")
                return redirect('accounts:register')
        else:
            messages.error(request, "Whoops! There was a problem registering the user. Try again.")
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html', {'user_form': user_form})




# Remove or comment out @login_required for development
# @login_required
def profile(request):
    # if not request.user.is_authenticated:
    #     # Handle anonymous users during development
    #     return redirect('profile')  # Redirect to home page or show a message

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:profile')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'accounts/profile.html', {'profile_form': profile_form})
