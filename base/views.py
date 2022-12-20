from django.shortcuts import render

from .models import Info

def l(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    return render(request, 'landing.html', {'u':u})

# Contact

def c(request):

    return render(request, 'c.html')

# Info

def t(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Договор-оферта'), 'i': 'a'})

def p(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Политика конфиденциальности'), 'i': 'p'})

def j(request):

    return render(request, 'info/juridical.html')

def ops(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Безопасность онлайн платежей'), 'i': 'ps'})
    
def ds(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Безопасность данных'), 'i': 'ds'})
