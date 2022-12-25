from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required as lr

from datetime import datetime as dt
from datetime import timezone

from .models import *

@lr
def home(request):

    c = {}
    c['home'] = True

    c['folders'] = Folder.objects.filter(user = request.user)

    notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False)

    p_notes = notes.filter(p = True)
    other_notes = notes.filter(p = False)

    c['p_notes'] = p_notes
    c['other_notes'] = other_notes

    c['profile'] = request.user.p


    return render(request, 'home.html', c)

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

    f = [Folder.objects.get(uid)]

    c = {}

    c['folder'] = f

    return render(request, 'components/notes.html', c)

@lr
def trash(request):

    c = {}

    notes = list(Note.objects.filter(user = request.user).filter(deleted = True))

    for note in notes:

        difference = dt.now(timezone.utc) - note.deleted_at

        if difference.total_seconds() > 604800:

            notes.remove(note)
            note.delete()

    c['notes'] = notes

    c['trash'] = True 

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

    Note.objects.create(

        user = request.user,

        title = request.POST.get('ti'),
        content = request.POST.get('c'),

        p = p,
        loved = loved,

    )

    c = {}

    current_folder = request.POST.get('cf')

    if current_folder:

        notes = Note.objects.filter(user = request.user).filter(folders__contains = [current_folder]).filter(deleted = False).filter(archived = False).filter(loved = False)

    else:

        notes = Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = False)

    p_notes = notes.filter(p = True)
    other_notes = notes.filter(p = False)

    c['p_notes'] = p_notes
    c['other_notes'] = other_notes

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
        title = request.POST.get('ft'),

    )

    return render(request, 'components/folders.html', {'folders': Folder.objects.filter(user = request.user)})

@lr
def edit_folder(request):

    folder = Folder.objects.get(uid = request.POST.get('u'))
    folder.title = request.POST.get('t')
    folder.save()

    return HttpResponse('K')

@lr
def delete_folder(request):

    Folder.objects.get(uid = request.POST.get('u')).delete()

    return render(request, 'components/folders.html', {'folders': Folder.objects.filter(user = request.user)})


@lr
def delete_deleted_notes(request):

    Note.objects.filter(user = request.user).filter(deleted = True).delete()

    return render(request, 'components/notes.html', {'notes': None, 'trash': True})