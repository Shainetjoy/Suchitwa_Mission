from django.urls import path
from smApp import views


urlpatterns = [
    path('', views.index,name= 'index'),
    path('signin', views.signin,name = 'signin'),
    path('signup',views.signup,name = 'signup'),


]