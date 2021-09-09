from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import RegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='student'))
