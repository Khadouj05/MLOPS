import requests

URL = "http://localhost:8000"

# 1. L'API est-elle en vie ?
print("GET /health ->", requests.get(URL + "/health").json())

# 2. Un client a faible consommation et faible anciennete
client = {"age": 35, "salaire": 2500, "abonnement": "Standard", "anciennete": 1, "consommation": 10}
r = requests.post(URL + "/predict", json=client)
print("POST /predict (client 1) ->", r.status_code, r.json())

# 3. Un client fidele : forte consommation, forte anciennete
client2 = {"age": 50, "salaire": 4000, "abonnement": "Premium", "anciennete": 10, "consommation": 80}
r2 = requests.post(URL + "/predict", json=client2)
print("POST /predict (client 2) ->", r2.status_code, r2.json())

# 4. Une erreur volontaire : l'age est du texte
mauvais = dict(client, age="abc")
r = requests.post(URL + "/predict", json=mauvais)
print("POST /predict (age='abc') ->", r.status_code)
print("Message :", r.json()["detail"][0]["msg"])
