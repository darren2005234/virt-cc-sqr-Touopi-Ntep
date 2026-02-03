<<<<<<< HEAD

# Frontend – Calculatrice Cloud Native

Ce dossier contient le frontend de l’application.

## Description

Le frontend est une interface web simple permettant :

- de saisir une opération (addition, soustraction, multiplication, division)
- d’envoyer une demande de calcul à l’API backend
- de récupérer le résultat d’un calcul à partir de son identifiant

## Technologies utilisées

- HTML
- CSS
- JavaScript
- Nginx

## Docker

Le frontend est servi via un conteneur Nginx.

### Construction de l’image

```bash
docker build -t calculatrice-frontend-darren-marie .
=======
Frontend – Interface Utilisateur

Présentation générale

Le frontend constitue la partie visible de l’application de calculatrice cloud native. Il fournit une interface web permettant à l’utilisateur de soumettre des opérations mathématiques et de consulter leurs résultats.

Il communique exclusivement avec le backend via l’API REST.


---

Rôle du frontend

Le frontend a pour missions :

afficher une interface simple et intuitive,

collecter les données saisies par l’utilisateur,

envoyer les requêtes au backend,

afficher les résultats des calculs.


Il ne contient aucune logique métier complexe, celle-ci étant déléguée au backend et au consumer.


---

Fonctionnalités

Le frontend permet :

le choix du type d’opération (addition, soustraction, multiplication, division, etc.),

la saisie des opérandes,

l’envoi de la requête de calcul,

l’affichage du résultat ou d’un message d’attente.



---

Communication avec le backend

Le frontend communique avec le backend via des requêtes HTTP :

POST vers l’endpoint /api/calculate

GET vers l’endpoint de récupération des résultats


Les échanges sont effectués au format JSON.


---

Architecture

Le frontend est une application web légère, conteneurisée avec Docker et déployée sur Kubernetes.

Il est exposé vers l’extérieur via un Ingress Kubernetes, ce qui permet un accès depuis un navigateur web standard.


---

Conteneurisation

Le frontend dispose d’un Dockerfile dédié permettant :

la construction de l’application web,

la création d’une image légère,

le déploiement automatisé sur Kubernetes.


Les images sont stockées dans un registre Docker.


---

Déploiement Kubernetes

Le frontend est déployé à l’aide :

d’un ReplicaSet garantissant la disponibilité,

d’un Service de type ClusterIP,

d’un Ingress pour l’exposition publique.



---

Bonnes pratiques

séparation frontend / backend

aucune donnée sensible stockée côté client

configuration externalisée

simplicité de l’interface utilisateur



---

Conclusion

Le frontend fournit une interface claire et accessible, complétant efficacement l’architecture microservices de la calculatrice cloud native.
>>>>>>> marie
