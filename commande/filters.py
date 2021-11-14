import django_filters
from .models import Commande


class CommandeFiltre(django_filters.FilterSet):
    class Meta:
        model=Commande
        fields='__all__'
        exclude=['client','Date_de_creation']




