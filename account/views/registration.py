from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import RegistrationForm
from django.contrib.auth import login,authenticate

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password =password)
            login(request,user)
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'pages/registration.html', context={
        'form': form
    })