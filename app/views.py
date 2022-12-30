from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required as lr

from datetime import datetime as dt
from datetime import timezone

from .models import *

@lr
def home(request):

    c = {}
    c['h'] = True

    c['folders'] = Folder.objects.filter(user = request.user)

    notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False)

    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)

    c['p'] = request.user.p

    return render(request, 'home.html', c)

def all(request):

    notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False)

    c = {}
    c['h'] = True

    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)

    return render(request, 'components/notes.html', c)

@lr
def l(request):

    c = {}
    c['l'] = True

    notes = Note.objects.filter(user = request.user).filter(loved = True)

    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)


    return render(request, 'components/notes.html', c)

@lr
def a(request):

    c = {}
    c['a'] = True

    notes = Note.objects.filter(user = request.user).filter(archived = True)


    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)

    return render(request, 'components/notes.html', c)

@lr
def s(request):

    q = request.POST.get('q')

    if q == '':

        n = None
        c['es'] = True

    else:

        n1 = list(Note.objects.filter(title__contains = q))
        n2 = list(Note.objects.filter(content__contains = q))
        n = set(n1 + n2)

    c = {}
    c['s'] = True

    c['n'] = n

    return render(request, 'components/notes.html', c)

@lr
def n(request, uid):
    return render(request, 'components/note.html', {'note': Note.objects.get(uid = uid)})

@lr
def f(request, uid):

    f = Folder.objects.get(uid = uid)

    c = {}
    c['f'] = f

    notes = Note.objects.filter(folders__in = [f]).filter(deleted = False).filter(archived = False)

    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)

    return render(request, 'components/notes.html', c)

@lr
def t(request):

    c = {}
    c['t'] = True 

    notes = list(Note.objects.filter(user = request.user).filter(deleted = True))

    for note in notes:

        difference = dt.now(timezone.utc) - note.deleted_at

        if difference.total_seconds() > 604800:

            notes.remove(note)
            note.delete()

    c['notes'] = notes


    return render(request, 'components/notes.html', c)

@lr
def create_note(request):

    p = request.POST.get('p')

    if p == 'on':
        p = True
    else:
        p = False

    loved = request.POST.get('l')

    if loved == 'on':
        loved = True
    else:
        loved = False

    note = Note.objects.create(

        user = request.user,

        title = request.POST.get('ti'),
        content = request.POST.get('c'),

        p = p,
        loved = loved,

    )

    folder_uids = request.POST.get('fu')

    if folder_uids:

        folder_uids = folder_uids.split(' ')

        for uid in folder_uids:

            folder = Folder.objects.get(uid = uid)
            note.folders.add(folder)
    
    c = {}

    current_folder = request.POST.get('cf')
    
    if current_folder:
        
        current_folder = Folder.objects.get(uid = current_folder)
        c['f'] = current_folder
        notes = Note.objects.filter(user = request.user).filter(folders__in = [current_folder]).filter(deleted = False).filter(archived = False).filter(loved = False)

    elif request.POST.get('lp'):

        c['l'] = True
        notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False).filter(loved = True)

    else:  

        c['h'] = True
        notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False)

    
    c['pn'] = notes.filter(p = True)
    c['on'] = notes.filter(p = False)

    return render(request, 'components/notes.html', c)

@lr
def ut(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.title = request.POST.get('t')
    n.save()

    return HttpResponse('K')

@lr
def uc(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.content = request.POST.get('c')
    n.save()

    return HttpResponse('K')


@lr
def ln(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.loved = not n.loved
    n.save()

    return HttpResponse('K')

@lr
def pn(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.p = not n.p
    n.save()

    return HttpResponse('K')

@lr
def an(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.archived = not n.archived
    n.save()

    return HttpResponse('K')

@lr
def dn(request):

    n = Note.objects.get(uid = request.POST.get('u'))
    n.deleted = not n.deleted
    n.save()

    return HttpResponse('K')

@lr
def delete_note(request):

    note = Note.objects.get(uid = request.POST.get('u'))
    note.deleted = not note.deleted
    note.save()

    return HttpResponse('K')

@lr
def create_folder(request):

    print(request.POST)

    Folder.objects.create(

        user = request.user,
        title = request.POST.get('t'),

    )

    return render(request, 'components/folders.html', {'f': Folder.objects.filter(user = request.user)})

@lr
def edit_folder(request):

    folder = Folder.objects.get(uid = request.POST.get('u'))
    folder.title = request.POST.get('t')
    folder.save()

    return HttpResponse('K')

@lr
def rf(request):

    Note.objects.get(uid = request.POST.get('n')).folders.remove(Folder.objects.get(uid = request.POST.get('f')))

    return HttpResponse('K')

@lr
def delete_folder(request):

    Folder.objects.get(uid = request.POST.get('u')).delete()

    return render(request, 'components/folders.html', {'folders': Folder.objects.filter(user = request.user), 'h': True, })


@lr
def delete_deleted_notes(request):

    Note.objects.filter(user = request.user).filter(deleted = True).delete()

    return render(request, 'components/notes.html', {'notes': None, 't': True})