from celery import shared_task
from .models import Calcul
import re

@shared_task
def traiter_calcul(calcul_id):
    calcul = Calcul.objects.get(id=calcul_id)

    try:
        if not re.match(r'^[0-9+\-*/().\s]+$', calcul.expression):
            raise ValueError()

        calcul.resultat = eval(calcul.expression)
        calcul.statut = 'TERMINE'

    except Exception:
        calcul.statut = 'ERREUR'

    calcul.save()
