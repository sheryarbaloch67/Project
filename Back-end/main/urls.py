from django.urls import path
from . import views

urlpatterns = [
    path('', views.cover),
    path('signup', views.signup),
    path('signin', views.signin),
    path('dashboard', views.dashboard),
    path('profile', views.profile),
    path('add course', views.course),
    path('add lecture', views.lecture),
    path('all lectures', views.lectures),
    path('add mcqs', views.mcqs),
    path('activity', views.activity),
]
