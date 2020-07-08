from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

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
    return render(request, 'account/profile.html')   