from django.contrib.auth import forms
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    context = {'users':User.objects.all()}
    return render(request, 'users/index.html',context)

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Account Created')
        return redirect('users:index')
    context = {'form':form}
    return render(request,'users/register.html',context)