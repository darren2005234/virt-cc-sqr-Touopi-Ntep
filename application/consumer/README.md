# Consumer

Le consumer est implémenté via Celery et fonctionne comme un microservice
indépendant du backend.

## Rôle
- Consommer les tâches de calcul envoyées par l'API
- Exécuter les opérations
- Stocker les résultats (Redis)

## Implémentation
Le code source Celery est situé dans le backend Django afin de conserver
la compatibilité avec l'application.

Le consumer est néanmoins déployé comme un service indépendant via un
conteneur dédié.

## Lancement
```bash
docker build -t calculatrice-consumer-darren-marie .
docker run calculatrice-consumer-darren_marie
