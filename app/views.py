from django.shortcuts import render, HttpResponse

from django.contrib.auth.decorators import login_required as lr

from datetime import datetime as dt
from datetime import timezone

from .models import *

@lr
def home(request):

    c = {}

    c['folders'] = Folder.objects.filter(user = request.user)

    notes = Note.objects.filter(user = request.user).filter(deleted = False)

    pinned_notes = notes.filter(pinned = True)
    other_notes = notes.filter(pinned = False)

    c['pinned_notes'] = pinned_notes
    c['other_notes'] = other_notes

    c['section'] = 'Дом'

    c['profile'] = request.user.p


    return render(request, 'home.html', c)

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

    pinned = request.POST.get('p')

    if pinned == 'on':
        pinned = True
    else:
        pinned = False

    loved = request.POST.get('l')

    if loved == 'on':
        loved = True
    else:
        loved = False

    Note.objects.create(

        user = request.user,

        title = request.POST.get('t'),
        content = request.POST.get('c'),

        pinned = pinned,
        loved = loved,

    )

    c = {}

    current_folder = request.POST.get('cf')

    if current_folder:

        pass

    else:

        notes = Note.objects.filter(user = request.user).filter(deleted = False)

        pinned_notes = notes.filter(pinned = True)
        other_notes = notes.filter(pinned = False)

        c['pinned_notes'] = pinned_notes
        c['other_notes'] = other_notes

    return render(request, 'components/notes.html', c)

@lr
def delete_note(request):

    note = Note.objects.get(uid = request.POST.get('u'))
    note.deleted = not note.deleted
    note.save()

    return HttpResponse('K')

@lr
def create_folder(request):

    Folder.objects.create(

        user = request.user,
        title = request.POST.get('t'),

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