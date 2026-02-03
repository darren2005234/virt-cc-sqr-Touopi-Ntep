Projet Calculatrice Cloud Native – Virtualisation & Cloud Computing

Informations générales

Module : Virtualisation & Cloud Computing
Établissement : Polytech Dijon – Université de Bourgogne
Année : Master

Binôme :

TOUOPI NGOUAGNA Darren Bryan
NTEP Marie Grâce



---

Objectif du projet :

Ce projet a pour objectif la conception, le développement et le déploiement d’une calculatrice Cloud Native, en appliquant les bonnes pratiques vues en cours de Virtualisation et Cloud Computing.

L’approche suivie est celle d’une application moderne orientée microservices, déployée sur un cluster Kubernetes, avec une infrastructure définie intégralement en Infrastructure as Code (IaC) via Terraform.

L’application permet à un utilisateur :

de soumettre un calcul (addition, soustraction, multiplication, division),

d’obtenir un identifiant unique pour ce calcul,

de récupérer le résultat ultérieurement via cet identifiant.



---

Architecture globale du projet

Le projet est découpé en trois grandes parties, chacune isolée dans un dossier dédié :

.
├── foundation/     # Infrastructure as Code (Terraform – Scaleway)
├── kubernetes/     # Déploiement Kubernetes (manifests YAML)
├── application/    # Code applicatif (frontend, backend, consumer)
└── README.md       # Rapport global du projet

Cette séparation permet :

une meilleure lisibilité du projet,

une maintenance facilitée,

une conformité avec les standards professionnels Cloud Native.



---

Choix technologiques

Infrastructure

Terraform : définition de l’infrastructure en code

Scaleway : fournisseur cloud français

DNS : résolution des noms de domaine pour les environnements de développement et de production


Orchestration et déploiement

Kubernetes : orchestration des conteneurs

Ingress NGINX : exposition des services HTTP


Application

Frontend : interface utilisateur web

Backend API : API REST pour la gestion des calculs

Redis : stockage clé/valeur des résultats

RabbitMQ : file d’attente pour le traitement asynchrone des calculs


Conteneurisation

Docker : création des images de chaque microservice



---

Déroulé du projet

1. Conception de l’architecture

Définition des microservices

Choix des technologies



2. Mise en place de l’infrastructure (foundation)

Cluster Kubernetes

Registre de conteneurs

Bases de données

LoadBalancers

Entrées DNS



3. Déploiement Kubernetes (kubernetes)

Création d’un namespace dédié au binôme

Déploiement des ReplicaSets et Services

Mise en place de l’Ingress



4. Développement applicatif (application)

API REST

Consommateur RabbitMQ

Interface utilisateur

Connexion Redis



5. Dockerisation et intégration

Création des Dockerfiles

Construction des images

Préparation au déploiement





---

Sécurité et bonnes pratiques

Les fichiers sensibles (ex : student.json) ne sont jamais versionnés

Utilisation de .gitignore pour protéger les clés et secrets

Séparation claire des responsabilités entre les composants

Variables d’environnement pour la configuration des services



---

Contenu des rapports

Chaque dossier contient un README.md servant de rapport détaillé :

foundation/README.md : description complète de l’infrastructure Terraform

kubernetes/README.md : description des manifestes Kubernetes et du déploiement

application/README.md : description des microservices, Dockerfiles et flux applicatifs


Ces documents constituent le rapport technique du projet.


---

État du projet

Infrastructure décrite en Terraform

Application microservices fonctionnelle

Déploiement Kubernetes opérationnel

Respect des exigences pédagogiques du module



---

Conclusion

Ce projet met en pratique l’ensemble des notions clés du Cloud Computing moderne : Infrastructure as Code, conteneurisation, orchestration Kubernetes et communication asynchrone entre microservices.

Il reflète une approche professionnelle de mise en production d’une application Cloud Native, en respectant les contraintes de sécurité, de maintenabilité et de scalabilité.