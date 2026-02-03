Backend – API Calculatrice Cloud Native

Présentation générale

Ce composant correspond à l’API backend de la Calculatrice Cloud Native. Il joue un rôle central dans l’architecture microservices du projet. L’API agit comme point d’entrée pour les requêtes des utilisateurs (via le frontend) et assure l’orchestration entre les différents services techniques : RabbitMQ pour la mise en file d’attente des calculs et Redis pour le stockage des résultats.

Le backend est conçu selon les bonnes pratiques Cloud Native : service stateless, conteneurisé avec Docker et déployé dans Kubernetes.


---

Responsabilités du backend

Le backend assure les fonctionnalités suivantes :

Exposer une API HTTP REST accessible par le frontend

Recevoir les demandes de calcul (addition, soustraction, multiplication, division)

Générer un identifiant unique pour chaque opération

Publier les calculs à effectuer dans une file RabbitMQ

Interroger Redis afin de récupérer les résultats des calculs

Retourner les réponses appropriées au frontend (succès, erreur, résultat non disponible)



---

Technologies utilisées

Langage : Python 3

Framework web : Flask

Broker de messages : RabbitMQ

Base de données clé/valeur : Redis

Conteneurisation : Docker

Orchestration : Kubernetes



---

Endpoints de l’API

L’API est versionnée et préfixée afin de faciliter son évolution.

1. Demande de calcul

Endpoint

POST /api/calculate

Description
Permet d’envoyer une demande de calcul au système.

Exemple de payload JSON

{
  "operation": "addition",
  "a": 10,
  "b": 5
}

Traitement côté backend

1. Génération d’un identifiant unique (UUID)


2. Création d’un message contenant l’opération et les opérandes


3. Envoi du message dans la file RabbitMQ


4. Retour immédiat de l’identifiant au client



Réponse

{
  "id": "c3b7c1a0-xxxx-xxxx-xxxx-xxxxxxxx"
}


---

2. Récupération du résultat

Endpoint

GET /api/result/<id>

Description
Permet de récupérer le résultat d’un calcul à partir de son identifiant.

Traitement côté backend

Interrogation de Redis avec la clé correspondant à l’ID

Si le résultat existe, il est retourné

Sinon, une erreur 404 est renvoyée


Réponse succès

{
  "result": 15
}

Réponse erreur

{
  "error": "Resultat non disponible"
}


---

Gestion des données avec Redis

Le backend ne stocke aucune donnée en mémoire locale.

Structure des données

Clé : identifiant unique du calcul (UUID)

Valeur : résultat du calcul


Exemple

SET c3b7c1a0-xxxx-xxxx-xxxx-xxxxxxxx 15
GET c3b7c1a0-xxxx-xxxx-xxxx-xxxxxxxx

Cette approche garantit la persistance des résultats même en cas de redémarrage du backend.


---

Communication avec RabbitMQ

À chaque requête de calcul, le backend publie un message dans une file RabbitMQ.

Contenu du message

{
  "id": "uuid",
  "operation": "addition",
  "a": 10,
  "b": 5
}

Le backend ne consomme jamais les messages : cette responsabilité est déléguée au consumer.


---

Variables d’environnement

Les paramètres sensibles ou dépendants de l’environnement sont fournis via des variables d’environnement :

REDIS_HOST

REDIS_PORT

RABBITMQ_HOST

RABBITMQ_PORT


Ces variables sont injectées via Kubernetes.


---

Dockerisation

Le backend est conteneurisé afin de garantir sa portabilité.

Étapes principales du Dockerfile

Utilisation d’une image Python légère

Installation des dépendances (Flask, redis, pika)

Exposition du port de l’API

Lancement du serveur Flask



---

Déploiement Kubernetes

Dans Kubernetes, le backend est déployé via :

Un ReplicaSet assurant la haute disponibilité

Un Service de type ClusterIP pour la communication interne

Une règle Ingress pour l’exposition externe


Les ressources CPU et mémoire sont limitées conformément aux exigences du projet.


---

Bonnes pratiques appliquées

Service stateless

Séparation claire des responsabilités

Configuration externalisée

Communication asynchrone via message broker

Respect de l’architecture microservices



---

Conclusion

Le backend constitue le cœur fonctionnel de la Calculatrice Cloud Native. Il illustre l’utilisation conjointe d’une API REST, d’un système de messagerie et d’un stockage externe afin de proposer une application robuste, scalable et conforme aux principes du Cloud Computing moderne.
