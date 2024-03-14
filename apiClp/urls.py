from django.urls import path
from apiClp.views import DadosViewSet, dados_html_view

urlpatterns = [
    path(
        "api/dados/",
        DadosViewSet.as_view({"get": "list", "post": "create"}),
        name="dados-list",
    ),
    path(
        "api/dados/<int:pk>/",
        DadosViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
        name="dados-detail",
    ),
    path("dados-html/", dados_html_view, name="dados-html"),
]
