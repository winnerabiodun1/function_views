from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='courses_index'),
    path('signup', views.signup, name='courses_signup'),
    path('login', views.login, name='courses_login'),
    path('sign_out', views.sign_out, name='courses_sign_out'),
    path('password_reset', views.password_reset, name='courses_password_reset'),
]