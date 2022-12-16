from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home'),

]

ajax_urlpatterns = [

    path('create-note/', create_note, name = 'create-note'),
    path('create-folder/', create_folder, name = 'create-folder'),

    path('edit-folder/', edit_folder, name = 'edit-folder'),

]

htmx_urlpatterns = [

    path('delete-folder/', delete_folder, name = 'delete-folder'),

]


urlpatterns += ajax_urlpatterns
urlpatterns += htmx_urlpatterns
