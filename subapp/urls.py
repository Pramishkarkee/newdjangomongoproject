# from django.conf import admin
from django.urls import path,include
from .import views
urlpatterns=[
    path('',views.login,name="login"),
    path('index',views.index,name="index"),
    path('register',views.register,name="register"),
    path('submit_form',views.submit_form,name="submit_form"),
    # path('',views.login,name="index"),
    # path('',views.login,name="index")
]