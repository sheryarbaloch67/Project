from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover),
    path('signup', views.signup),
    path('signin', views.signin),
]
