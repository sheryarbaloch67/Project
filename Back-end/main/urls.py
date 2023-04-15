from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.cover, name='cover'),
    path('test', views.test, name='test'),
    path('signin/', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    # path('signin/<str:next_page>/', views.dashboard, name='signin_next'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('add course', views.course, name='course'),
    path('add lecture', views.lecture, name='lecture'),
    path('all lectures', views.lectures, name='lectures'),
    path('add mcqs', views.mcqs, name='mcqs'),
    path('activity', views.activity, name='activity'),
]

    # path('all lectures/<int:course_id>/', views.lectures, name='lectures'),