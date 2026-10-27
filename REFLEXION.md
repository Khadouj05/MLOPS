## TP3 - Suivi des experiences avec MLflow

### 1. Quel est le meilleur modele ? Peux-tu le prouver ?
L'Essai 1 et l'Essai 3 ont obtenu les meilleures performances (F1 = 0.889, Accuracy = 0.99). L'Essai 3 est retenu car il est plus simple et n'utilise pas la variable salaire. MLflow le prouve grace au tri des runs par metrics.f1.

### 2. Peux-tu redonner exactement le modele de l'Essai 1 ?
Oui, grace a son identifiant de run unique (Run ID) en utilisant la commande mlflow.sklearn.load_model("runs:/<RUN_ID>/model").

### 3. Un camarade peut-il reproduire ton travail sur une autre machine ?
Le code et les dependances sont conserves via Git et MLflow, mais un environnement identique necessitera Docker (TP5/TP6).

## TP4 - Registry de modeles et API FastAPI

### 1. Comment designer officiellement le modele a utiliser ?
Avec l'alias @champion (models:/churn-model@champion) dans le Model Registry de MLflow sur la version choisie.

### 2. Comment une application peut-elle utiliser le modele ?
En envoyant une requete HTTP POST au format JSON avec les donnees du client vers la route /predict de l'API FastAPI.

### 3. Que se passe-t-il quand on change de champion ?
On deplace l'alias @champion vers la nouvelle version dans le Registry et on redemarre l'API. Le code de l'API et des applications clientes reste inchange.
