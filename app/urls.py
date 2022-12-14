from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home')

]

ajax_urlpatterns = [



]

htmx_urlpatterns = [



]


urlpatterns += ajax_urlpatterns
urlpatterns += htmx_urlpatterns
