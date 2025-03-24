from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.createUser, name="add-user"),
    path("edit/", views.editUser, name="edit-user")
]
