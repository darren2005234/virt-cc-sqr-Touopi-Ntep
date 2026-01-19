from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Calcul
from .serializers import CalculSerializer
from .tasks import traiter_calcul

# Créer un calcul
@api_view(["POST"])
def create_calcul(request):
    serializer = CalculSerializer(data=request.data)
    if serializer.is_valid():
        # On crée le calcul avec le statut EN_ATTENTE
        calcul = serializer.save(statut="EN_ATTENTE")
        
        # Envoyer la tâche à Celery
        traiter_calcul.delay(calcul.id)
        
        # Retourner uniquement l'ID
        return Response({"id": str(calcul.id)}, status=201)
    
    # Si le serializer n'est pas valide, retourner les erreurs
    return Response(serializer.errors, status=400)


# Récupérer le calcul par ID
@api_view(["GET"])
def get_calcul(request, id):
    # Récupérer le calcul ou renvoyer 404 si introuvable
    calcul = get_object_or_404(Calcul, id=id)

    # Si le calcul est terminé, renvoyer le résultat
    if calcul.statut == "TERMINE":
        return Response({
            "statut": "TERMINE",
            "resultat": calcul.resultat
        })
    
    # Sinon renvoyer le statut actuel
    return Response({"statut": calcul.statut})
