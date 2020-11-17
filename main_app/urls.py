from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('add_project', views.add_project),
    path('create_project', views.create_project),
    path('logout', views.logout),
]