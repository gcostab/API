from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="disciplina-index"),
    path("add/", views.add, name="disciplina-add")
]