Projet Calculatrice Cloud Native – Virtualisation & Cloud Computing

Informations générales

Module : Virtualisation & Cloud Computing
Établissement : Polytech Dijon – Université de Bourgogne
Année : 4A - SQR

Binôme :

Touopi

Ntep



---

Objectif du projet

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