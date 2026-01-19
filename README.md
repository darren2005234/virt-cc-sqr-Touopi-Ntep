# virt-cc-sqr-Touopi-Ntep
Virtualisation et cloud computing

# MEMBRES DU GROUPE :

NTEP MARIE GRACE 
TOUOPI NGOUAGNA DARREN BRYAN


# OBJECTIF DU PROJET :
Réalisation d'une calculatrice Clou Native basée sur une architecture microservice déployée sur Kubernetes et provisionnée via Terraform


# Technologies utilisées :
-Terraform
-Kubernetes
-Docker
-Redis
-RabbitMQ
-GitHub
-Django

# Déroulé du projet

Le projet a été réalisé selon une approche Cloud Native :

1. Définition de l’infrastructure via Terraform (Scaleway)
2. Conteneurisation des microservices avec Docker
3. Architecture microservices avec :
   - Frontend
   - Backend API
   - Consumer asynchrone
4. Préparation du déploiement Kubernetes

---

# Architecture globale

- Terraform : registre, cluster Kubernetes, base de données, DNS, LoadBalancer
- Kubernetes : ReplicaSets, Services, Ingress
- Application : microservices conteneurisés