from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *

from django.conf import settings

app_name = 'u'

urlpatterns = [

    path('login/', log_in, name = 'li'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'lo'),
    path('register/', register, name = 'r'),

    path('ce/', ce, name = 'ce'),

    path('change-mode/', change_mode, name = 'm'),

]