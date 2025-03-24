from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista, name="read"),
    path("<int:pessoa_id>/", views.detail, name="detail"),
    path("add/", views.add, name="create"),
    path("edit/<int:pessoa_id>/", views.edit, name="update"),
    path("remove/<int:pessoa_id>/", views.remove, name="delete"),
    path("license-invalid/", views.license_invalid, name="license_invalid"),
    path("license-missing/", views.license_missing, name="license_missing"),
]