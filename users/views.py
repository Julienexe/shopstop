from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, LoginForm, ProfileForm

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)    
                return redirect ('shop:home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def  signup(request):
    if request.method=='POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email') 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request,user)
            return redirect ('shop:home')
    else:
       form = CustomUserCreationForm()     
    return render(request,'users/signup.html', {'form':form})  

def log_out(request):
    logout(request)
    return redirect('shop:home')

def profileform(request):
    form = ProfileForm()
    return render(request,'users/profile.html',{'form':form})
