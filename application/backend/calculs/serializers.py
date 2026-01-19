from rest_framework import serializers
from .models import Calcul

class CalculSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calcul
        fields = ['id', 'expression', 'resultat', 'statut']
        read_only_fields = ['id', 'resultat', 'statut']
