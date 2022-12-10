from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('logout', views.logout,name='logout'),
    path('index', views.index,name='index'),
]
