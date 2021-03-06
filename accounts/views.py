from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, ProfileRegistrationForm
from django.urls import reverse
from django.contrib import messages, auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
def get_home(request): 
    return render(request, 'index.html')
    

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username_or_email_input = login_form.cleaned_data['username_or_email']
            password_input = login_form.cleaned_data['password']
            user = authenticate(username=username_or_email_input, password=password_input)
    
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'forms': login_form})
    
    
def signup(request): 
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            username_input = user_form.cleaned_data['username']
            password_input = user_form.cleaned_data['password1']
            user = authenticate(username=username_input, password=password_input)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()

    return render(request, "signup.html", {'form': user_form, 'profile_form': profile_form})
    
    
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

@login_required(login_url='/accounts/login')
def profile(request):
    return render(request, 'profile.html')