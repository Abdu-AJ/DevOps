from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("NewTicket", views.NewTicket, name='NewTicket'),
    path("Tracking", views.Tracking, name='Tracking'),
    path("Result", views.Result, name='Result'),
]