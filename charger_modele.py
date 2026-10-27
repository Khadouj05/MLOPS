import mlflow
import mlflow.sklearn
import pandas as pd

# 1. Retrouver l'ID du meilleur run
runs = mlflow.search_runs(
    experiment_names=["churn-prediction"],
    order_by=["metrics.f1 DESC"]
)
run_id = runs.iloc[0]["run_id"]

# 2. Recharger le modèle sauvegardé dans ce run
model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")
print("Modèle rechargé :", type(model).__name__)

# 3. Tester sur un nouveau client
client = pd.DataFrame([{
    "age": 35, "salaire": 2500, "anciennete": 1, "consommation": 10,
    "abonnement_Premium": False, "abonnement_Standard": True,
}])

client = client[list(model.feature_names_in_)]
prediction = model.predict(client)[0]
print("Le client va-t-il partir ? ->", "OUI" if prediction == 1 else "NON")