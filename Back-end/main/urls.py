from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.cover, name='cover'),
    path('test', views.test, name='test'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('add course', views.course, name='course'),
    path('all lectures/<int:course_id>/', views.lectures, name='lectures'),
    path('add lecture/<int:course_id>/', views.lecture, name='lecture'),
    path('add_mcqs/<int:course_id>/<int:lecture_id>/', views.add_mcqs, name='add_mcqs'),
    path('activity', views.activity, name='activity'),
]

    # path('all lectures/<int:course_id>/', views.lectures, name='lectures'),