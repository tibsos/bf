from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import *

from django.conf import settings

app_name = 'user'

urlpatterns = [

    path('login/', log_in, name = 'login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'register'),
    path('register/', register, name = 'register'),

]