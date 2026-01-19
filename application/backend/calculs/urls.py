from django.urls import path
from .views import create_calcul, get_calcul

urlpatterns = [
    path("api/calcul/", create_calcul),
    path("api/calcul/<uuid:id>/", get_calcul),
]


