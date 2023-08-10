from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('api/<int:pk>', views.usersdetails, name='usersdetails' ),
]
