Kubernetes – Déploiement de la Calculatrice Cloud Native

Objectif de cette section

Cette section décrit la configuration Kubernetes permettant le déploiement et l’exécution de l’application Calculatrice Cloud Native sur un cluster Kubernetes.

L’objectif est de :

déployer l’ensemble des microservices de l’application,

assurer leur communication interne,

exposer les services nécessaires vers l’extérieur,

respecter les bonnes pratiques Kubernetes vues en cours.



---

Namespace

L’ensemble des ressources Kubernetes est déployé dans un namespace dédié au binôme, afin de :

isoler les ressources,

éviter les conflits avec d’autres projets,

faciliter la gestion et le nettoyage.


Exemple de namespace utilisé :

<prenom1>-<prenom2>

Toutes les ressources (ReplicaSet, Service, Ingress) sont déclarées dans ce namespace.


---

Microservices déployés

Les microservices suivants sont déployés dans le cluster Kubernetes :

Frontend : interface utilisateur

Backend API : gestion des requêtes HTTP

Consumer : traitement asynchrone des calculs

Redis : stockage des résultats

RabbitMQ : file d’attente des calculs

PostgreSQL (si utilisé) : base de données applicative


Chaque microservice est déployé à l’aide d’un ReplicaSet et exposé via un Service lorsque nécessaire.


---

ReplicaSets

Rôle

Les ReplicaSet garantissent qu’un nombre défini de pods est toujours en cours d’exécution, assurant ainsi :

la résilience,

la disponibilité des services,

la possibilité de montée en charge.


Chaque microservice dispose de son propre ReplicaSet.

Ressources allouées

Conformément aux consignes du projet, chaque conteneur définit explicitement des ressources minimales :

resources:
  requests:
    cpu: "4m"
    memory: "32Mi"

Ces paramètres permettent une meilleure gestion des ressources par Kubernetes.


---

Services Kubernetes

Rôle

Les Service permettent :

l’exposition des pods à l’intérieur du cluster,

la communication entre microservices,

la stabilité des points d’accès malgré le redémarrage des pods.


Services déclarés

svc-frontend

svc-backend

svc-redis

svc-rabbitmq

svc-postgresql (si applicable)


Les services internes utilisent le type ClusterIP.


---

Variables d’environnement

Les informations de connexion entre microservices sont passées via des variables d’environnement, notamment :

adresse du service Redis

adresse du service RabbitMQ

ports de communication


Cela permet de :

découpler la configuration du code,

faciliter le déploiement sur différents environnements.



---

Ingress

Rôle

Un objet Ingress est utilisé pour exposer les services frontend et backend API vers l’extérieur du cluster.

L’Ingress s’appuie sur l’Ingress Controller NGINX, déjà présent dans le cluster.

Configuration

ingressClassName: nginx

Routage basé sur le nom de domaine

Routage des chemins :

/ → frontend

/api → backend



Les noms de domaine utilisés correspondent à ceux définis dans la section foundation.


---

Flux réseau

Le fonctionnement réseau global est le suivant :

L’utilisateur accède à l’application via le navigateur

La requête arrive sur l’Ingress

L’Ingress redirige vers le service frontend ou backend

Le backend communique avec Redis et RabbitMQ via les services internes

Le consumer consomme les messages RabbitMQ et stocke les résultats dans Redis



---

Schéma récapitulatif Kubernetes

graph LR
  subgraph Kubernetes
    subgraph Namespace
      FrontRS[Frontend ReplicaSet] --> FrontPod[Pod Frontend]
      ApiRS[API ReplicaSet] --> ApiPod[Pod API]
      ConsRS[Consumer ReplicaSet] --> ConsPod[Pod Consumer]
      RedisRS[Redis ReplicaSet] --> RedisPod[Pod Redis]
      RabbitRS[RabbitMQ ReplicaSet] --> RabbitPod[Pod RabbitMQ]

      SvcFront[Service Frontend] --> FrontPod
      SvcApi[Service API] --> ApiPod
      SvcRedis[Service Redis] --> RedisPod
      SvcRabbit[Service RabbitMQ] --> RabbitPod

      ApiPod -.-> SvcRedis
      ApiPod -.-> SvcRabbit
      ConsPod -.-> SvcRabbit
      ConsPod -.-> SvcRedis
    end
    Ingress --> SvcFront
    Ingress --> SvcApi
  end


---

Validation du déploiement

Les manifestes Kubernetes ont été :

validés syntaxiquement,

déployés sans erreur sur le cluster,

testés via l’accès au nom de domaine public.


L’accès à l’URL publique permet d’utiliser pleinement la calculatrice.


---

Conclusion

La configuration Kubernetes mise en place permet :

un déploiement fiable des microservices,

une communication maîtrisée entre les composants,

une exposition sécurisée vers l’extérieur.


Cette section complète l’infrastructure définie avec Terraform et l’application décrite dans la section application.