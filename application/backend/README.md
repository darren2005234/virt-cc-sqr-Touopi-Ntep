
# Backend – API Calculatrice

Ce dossier contient l’API backend de la calculatrice, développée avec Django.

## Fonctionnalités

L’API permet :

- de recevoir une demande de calcul (POST)
- de placer la demande dans une file RabbitMQ
- de récupérer le résultat d’un calcul via un identifiant (GET)

Les calculs sont traités de manière asynchrone.

## Technologies utilisées

- Python
- Django
- Django REST Framework
- Celery
- RabbitMQ

## Asynchrone & File d’attente

- L’API joue le rôle de **producer**
- RabbitMQ est la **file de messages**
- Celery est le **consumer**

Les tâches sont définies dans :

calculs/tasks.py
