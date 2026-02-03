<<<<<<< HEAD
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
=======
Application – Calculatrice Cloud Native


Présentation générale

Cette section décrit l’application Cloud Native développée dans le cadre du projet de Virtualisation & Cloud Computing.

L’application est conçue selon une architecture microservices, permettant :

une meilleure séparation des responsabilités,

une montée en charge facilitée,

une meilleure résilience en cas de défaillance d’un composant.


L’objectif fonctionnel est de proposer une calculatrice distribuée, capable de traiter des calculs de manière asynchrone et de stocker les résultats de façon persistante.


---

Architecture applicative

L’application est composée de cinq services principaux :

1. Frontend : interface utilisateur


2. Backend (API) : gestion des requêtes HTTP


3. RabbitMQ : file d’attente pour les calculs


4. Consumer : traitement des calculs


5. Redis : stockage des résultats



Schéma d’architecture

graph TB
    U[Utilisateur] --> F[Frontend]
    F -->|HTTP| B[Backend API]
    B -->|Publication message| Q[RabbitMQ]
    C[Consumer] -->|Consommation message| Q
    C -->|Stockage résultat| R[(Redis)]
    B -->|Lecture résultat| R


---

Organisation du dossier application

application/
├── frontend/     # Interface utilisateur
├── backend/      # API REST
├── consumer/     # Consommateur RabbitMQ
└── README.md     # Documentation applicative

Chaque sous-dossier correspond à un microservice indépendant, conteneurisé via Docker.


---

Backend – API REST

Rôle

Le backend est une API REST chargée de :

recevoir les demandes de calcul,

générer un identifiant unique pour chaque opération,

publier les calculs dans une file RabbitMQ,

permettre la récupération des résultats stockés dans Redis.


Endpoints disponibles

➕ Soumission d’un calcul

Méthode : POST

Route : /api/calculate


Corps de la requête :

{
  "operation": "addition",
  "a": 5,
  "b": 3
}

Réponse :

{
  "id": "uuid-calcul"
}


---

Récupération d’un résultat

Méthode : GET

Route : /api/result/<id>


Réponse si résultat disponible :

{
  "result": 8
}

Réponse si résultat indisponible :

404 Not Found


---

RabbitMQ – File d’attente

Rôle

RabbitMQ est utilisé pour découpler la réception des calculs de leur exécution.

À chaque demande de calcul :

l’API publie un message contenant l’opération et les opérandes,

le consumer récupère le message de manière asynchrone.


Format des messages

{
  "id": "uuid-calcul",
  "operation": "multiplication",
  "a": 4,
  "b": 6
}


---

Consumer – Traitement des calculs

Rôle

Le consumer est un service indépendant chargé de :

consommer les messages RabbitMQ,

effectuer le calcul demandé,

stocker le résultat dans Redis.


Opérations supportées

Addition

Soustraction

Multiplication

Division (avec gestion des erreurs)



---

Redis – Stockage des résultats

Rôle

Redis est utilisé comme base de données clé/valeur, permettant :

un accès rapide aux résultats,

une persistance même si l’API redémarre.


Structure des données

Clé : identifiant du calcul

Valeur : résultat du calcul


Exemple :

clé   : "uuid-calcul"
valeur: "8"


---

Frontend – Interface utilisateur

Rôle

Le frontend permet à l’utilisateur de :

saisir une opération mathématique,

envoyer une demande de calcul à l’API,

récupérer le résultat à partir d’un identifiant.


Il communique exclusivement avec l’API backend via HTTP.


---

Dockerisation

Chaque microservice dispose de son Dockerfile :

backend/Dockerfile

frontend/Dockerfile

consumer/Dockerfile


Commandes de build des images

docker build -t calculatrice-backend ./backend
docker build -t calculatrice-frontend ./frontend
docker build -t calculatrice-consumer ./consumer

Push vers Google Artifact Registry

docker tag calculatrice-backend <registry>/calculatrice-backend:latest
docker push <registry>/calculatrice-backend:latest


---

Sécurité et bonnes pratiques

Aucun secret n’est stocké dans le dépôt Git

Les configurations sensibles sont passées via variables d’environnement

Le fichier student.json est ignoré via .gitignore



---

Conclusion

L’application respecte pleinement les principes Cloud Native :

microservices indépendants,

communication asynchrone,

stockage externe,

conteneurisation complète.


Elle est conçue pour être déployée facilement sur Kubernetes et s’intègre parfaitement avec l’infrastructure définie dans la section foundation.
>>>>>>> marie
