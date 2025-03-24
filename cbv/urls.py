from django.urls import path
from .views import PessoaView, PessoaListView, PessoaAddView, PessoaEditView, PessoaDelView

urlpatterns = [
    path('', PessoaView.as_view(), name='pessoa'),
    path('list/', PessoaListView.as_view(), name='pessoa_list'),
    path('add/', PessoaAddView.as_view()),
    path('update/<int:pk>/', PessoaEditView.as_view()),
    path('delete/<int:pk>/', PessoaDelView.as_view()),
]