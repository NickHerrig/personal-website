from django.urls import path 

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='books'),
    path('login', views.LoginPageView.as_view(), name='login'),
]
