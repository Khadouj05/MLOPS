import mlflow

# Récupérer tous les runs triés par le score F1 (décroissant)
runs = mlflow.search_runs(
    experiment_names=["churn-prediction"],
    order_by=["metrics.f1 DESC"]
)

colonnes = ["tags.mlflow.runName", "params.n_estimators", "params.max_depth", "metrics.accuracy", "metrics.f1"]
print(runs[colonnes].to_string(index=False))

meilleur = runs.iloc[0]
print("\nMeilleur run :", meilleur["tags.mlflow.runName"], "| ID :", meilleur["run_id"][:8])