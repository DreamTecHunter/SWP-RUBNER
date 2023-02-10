import requests

# ...
# Normaler Code

# dieser Code wird benötigt um Daten an die FlaskAPI zu senden
response = requests.post(
    # TODO: /route von Route von der FlaskAPI
    "http://127.0.0.1:8888/route",
    # hier wird eine dict übergeben, kann auch eine Liste oder ein andere sequenzieller Datentyp sein
    json={
        "key": "value",
        "hand2": "value",
        "...": "..."
    }
)

# ...
# restlicher Code
