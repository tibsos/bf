from django.urls import path

from .views import *

app_name = 'a'

urlpatterns = [

    path('home/', home, name = 'home'),

]

ajax_urlpatterns = [

    path('delete-note/', delete_note, name = 'delete-note'),
    
    path('edit-folder/', edit_folder, name = 'edit-folder'),
    path('rf/', rf, name = 'rf'),

    path('ut/', ut, name='ut'),
    path('uc/', uc, name='uc'),

    path('ln/', ln, name='ln'),
    path('pn/', pn, name='pn'),
    path('an/', an, name='an'),
    path('dn/', dn, name='dn'),

]

htmx_urlpatterns = [

    path('s/', s, name = 's'), # search
    path('all/', all, name = 'all'),
    path('loved/', l, name = 'l'), 
    path('f/<uuid:uid>/', f, name = 'f'),
    path('archived/', a, name = 'a'), 
    path('trash/', t, name = 't'),

    path('n/<uuid:uid>/', n, name = 'n'),

    path('create-note/', create_note, name = 'create-note'),

    path('create-folder/', create_folder, name = 'create-folder'),
    path('delete-folder/', delete_folder, name = 'delete-folder'),

    path('delete-deleted-notes/', delete_deleted_notes, name = 'delete-deleted-notes'),

]


urlpatterns += ajax_urlpatterns
urlpatterns += htmx_urlpatterns
