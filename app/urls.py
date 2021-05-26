from django.urls import path,include
from .views import home,team,contactUs



app_name='app'

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('team',team.as_view(),name='team'),
    path('contactUs',contactUs.as_view(),name='contact'),



]
