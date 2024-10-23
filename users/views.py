from django.shortcuts import render, redirect
from users.forms import LoginForms, RegisterForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    form = LoginForms(request.POST)
    if request.method == 'POST' and form.is_valid():
        name = form['name'].value()
        password = form['password'].value()
        if name and password:
            user = auth.authenticate(
                request,
                username=name,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login efetuado!')
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos!')
                return redirect('login')
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForms(request.POST)
    if request.method == 'POST' and form.is_valid():
        # TODO criacao usuario
        name = form['name'].value()
        email = form['email'].value()
        password = form['password'].value()

        user_exist = User.objects.filter(username=name)
        if user_exist:
            messages.error(request, 'Usuário já existente!')
            return redirect('register')
        
        new_user = User.objects.create_user(
            username=name,
            email=email,
            password = password
        )
        new_user.save()
        messages.success(request, 'Usuário registrado com sucesso!')
        return redirect('login')
    
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Usuário deslogado!')
    return redirect('login')