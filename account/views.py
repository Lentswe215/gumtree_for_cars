from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UpdateProfileForm

# Create your views here.
def login(request):
    return render(request, 'account/login_form.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created!')
            return redirect('/account/login') 
        
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

@login_required
def profile(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account Updated!')
            return redirect('/account/profile') 

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form':profile_form
    }
    return render(request, 'account/profile.html', context)   