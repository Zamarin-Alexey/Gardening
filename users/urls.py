from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('reg/', registration, name='registration')
]
