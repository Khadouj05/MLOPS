## TP3 - Suivi des experiences avec MLflow

### 1. Quel est le meilleur modele ? Peux-tu le prouver ?
L'Essai 1 et l'Essai 3 ont obtenu les meilleures performances (F1 = 0.889, Accuracy = 0.99). L'Essai 3 est retenu car il est plus simple et n'utilise pas la variable salaire. MLflow le prouve grace au tri des runs par metrics.f1.

### 2. Peux-tu redonner exactement le modele de l'Essai 1 ?
Oui, grace a son identifiant de run unique (Run ID) en utilisant la commande mlflow.sklearn.load_model("runs:/<RUN_ID>/model").

### 3. Un camarade peut-il reproduire ton travail sur une autre machine ?
Le code et les dependances sont conserves via Git et MLflow, mais un environnement identique necessitera Docker (TP5/TP6).
