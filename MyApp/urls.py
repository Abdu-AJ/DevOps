from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("NewTicket", views.NewTicket, name='NewTicket'),
    path("Tracking", views.Tracking, name='Tracking'),
    path("Result", views.Result, name='Result'),
    path("Usage", views.User_Usage, name='Usage'),
    path("Usage_results", views.Usage_results, name='Usage_results'),
]