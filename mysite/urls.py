from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import urls
from cbv.api.viewsets import PessoaViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pessoas/api/', PessoaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pessoa/", include("pessoa.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("disciplina/", include("disciplina.urls")),
    path("cbv/", include("cbv.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]