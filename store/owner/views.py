from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password != password1:
            messages.error(request, "Your password and confirm password are not the same!")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
        else:
            User.objects.create_user(username, email, password)
            messages.success(request, "User created successfully!")
            return redirect('user_create')
    return render(request, "user_form.html")

def user_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']

        user.username = username
        user.email = email
        user.set_password(password)
        user.save()
        return redirect('user_list')
    return render(request, 'user_edit.html', {'user': user})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})
