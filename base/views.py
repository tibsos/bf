from django.shortcuts import render

from .models import Info

def l(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    return render(request, 'landing.html', {'u': u})

# Contact

def c(request):

    return render(request, 'c.html')

# Info

def t(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    c['d'] = Info.objects.get(title = 'Договор-оферта')
    c['i'] = 't'

    return render(request, 'info/terms.html', c)

def p(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    c['d'] = Info.objects.get(title = 'Политика конфиденциальности')
    c['i'] = 'p'

    return render(request, 'info/terms.html', c)

def j(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    return render(request, 'info/juridical.html', c)

""" def ops(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Безопасность онлайн платежей'), 'i': 'ps'})
    
def ds(request):

    return render(request, 'info/terms.html', {'d': Info.objects.get(title = 'Безопасность данных'), 'i': 'ds'})
 """


def plans(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    return render(request, 'info/plans.html', c)