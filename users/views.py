from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserCreationForm, LoginForm

#login page
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
                #return redirect('home')
    else:
        form = LoginForm()
    #return render(request, 'login.html', {'form': form})

