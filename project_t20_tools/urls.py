from django.urls import path
from app_t20_tools import views

urlpatterns = [
    # rota, view responsavel pela rota, nome de referencia
    # t20tools.com,
    path("", views.home, name="home"),
    path("racas", views.racas, name="racas"),
]
