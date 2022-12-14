from django.shortcuts import render

def landing(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    return render(request, 'landing.html', {'u':u})