from django.urls import path

from .views import *

app_name = 'base'

urlpatterns = [

    path('', landing, name = 'landing'),

]