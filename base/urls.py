from django.urls import path

from .views import *

app_name = 'b'

urlpatterns = [

    path('', l, name = 'l'),

    path('plans/', plans, name = 'pl'),

    path('contact-us/', c, name = 'c'),

    path('terms/', t, name = 't'),
    path('privacy/', p, name = 'p'),
    path('juridical-information/', j, name = 'j'),
    
    #path('online-payment-safety/', ops, name = 'ops'),
    #path('data-safety/', ds, name = 'ds'),

]