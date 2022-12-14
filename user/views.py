from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def log_in(request):

    c = {}

    if request.method == 'POST':

        u = authenticate(

            username = request.POST.get('u'),
            password = request.POST.get('p'),

        )

        if u:

            login(request, u)
            return redirect('/home/')

        else: 

            return render(request, 'auth/login.html', {'e': True})

    return render(request, 'auth/login.html')

def register(request):

    if request.method == 'POST':

        n = request.POST.get('n')

        u = request.POST.get('u')
        p = request.POST.get('p')

        u = User(username = u)
        u.set_password(p)
        u.save()

        u.p.name = n
        u.p.save()

        u = authenticate(username = u, password = p)
        login(request, u)

        return redirect('/home/')

    return render(request, 'auth/register.html')