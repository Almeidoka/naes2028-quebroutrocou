from django.urls import path
from .views import IndexView, ContatoView

urlpatterns = [
    # path("url/navegator", Class.as_view(), name="nome_do_link"),
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
]