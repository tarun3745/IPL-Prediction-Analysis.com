from django.urls import path

from . import views

urlpatterns=[
    path('',views.home, name='winWT'),
    path('winwot/',views.home2, name='winWOT'),
    path('score/',views.home3, name='score'),
    path('feedback/',views.home5, name='feedback'),
    path('mom/',views.home4, name='mom'),
    path('add/',views.add, name='add'),
    path('add2/',views.add2, name='add2'),
    path('add3/',views.add3, name='add3'),
    path('add4/',views.add4, name='add4'),
    path('add5/',views.add5, name='add5'),
    path('signup/',views.singup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
]