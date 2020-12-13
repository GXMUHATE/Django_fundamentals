from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("gracane", views.gracane, name="gracane"),
    path("muhate", views.muhate, name="muhate")
]