from django.shortcuts import render

from django.contrib.auth.decorators import login_required as lr

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


    return render(request, 'home.html', c)


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
def create_folder(request):

    Folder.objects.create(

        user = request.user,
        title = request.POST.get('t'),

    )

    return render(request, 'components/folders.html', {'folders': Folder.objects.filter(user = request.user)})