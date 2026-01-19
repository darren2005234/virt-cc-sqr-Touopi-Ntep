from django.db import models

# Create your models here.
import uuid


class Calcul(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expression = models.CharField(max_length=255)
    resultat = models.FloatField(null=True, blank=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('EN_ATTENTE', 'En attente'),
            ('TERMINE', 'Terminé'),
            ('ERREUR', 'Erreur')
        ],
        default='EN_ATTENTE'
    )
    created_at = models.DateTimeField(auto_now_add=True)
