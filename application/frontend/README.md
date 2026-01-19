
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
