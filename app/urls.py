from django.urls import path

from .views import *

app_name = 'a'

urlpatterns = [

    path('home/', home, name = 'home'),

]

ajax_urlpatterns = [

    
    path('delete-note/', delete_note, name = 'delete-note'),

    
    path('edit-folder/', edit_folder, name = 'edit-folder'),

]

htmx_urlpatterns = [

    #path('create-note-'),
    path('create-note/', create_note, name = 'create-note'),

    path('trash', trash, name = 'trash'),

    path('delete-deleted-notes/', delete_deleted_notes, name = 'delete-deleted-notes'),

    path('create-folder/', create_folder, name = 'create-folder'),
    path('delete-folder/', delete_folder, name = 'delete-folder'),

]


urlpatterns += ajax_urlpatterns
urlpatterns += htmx_urlpatterns
