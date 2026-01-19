# Application – Calculatrice Cloud Native

Ce dossier contient l’ensemble des microservices applicatifs du projet **Calculatrice Cloud Native**.

L’application est conçue selon une architecture **microservices**, conteneurisée avec Docker, et prête à être déployée sur Kubernetes.

---

##  Architecture applicative

L’application est composée de quatre services principaux :

- **Frontend** : interface utilisateur (HTML / CSS / JavaScript) servie via Nginx
- **Backend** : API REST développée avec Django
- **Consumer** : consommateur de messages (Celery worker)
- **RabbitMQ** : broker de messages pour la gestion des files d’attente

Les calculs sont traités de manière asynchrone via une file RabbitMQ et consommés par le worker Celery.

---