from celery import shared_task
from .models import Calcul
import re

@shared_task
def traiter_calcul(calcul_id):
    calcul = Calcul.objects.get(id=calcul_id)

    try:
        # Sécurité : on vérifie que l'expression est valide
        if not re.match(r'^[0-9+\-*/().\s]+$', calcul.expression):
            raise ValueError("Expression invalide")

        # Calcul effectif
        calcul.resultat = eval(calcul.expression)
        calcul.statut = 'TERMINE'
        
        # ON AJOUTE LE RETURN ICI !
        resultat_final = calcul.resultat

    except Exception:
        calcul.statut = 'ERREUR'
        resultat_final = "Erreur de calcul"

    calcul.save()
    return resultat_final # <--- C'est cette ligne qui remplit Redis !
