import requests

url = "http://127.0.0.1:8000/exoplanets/create/"
data = {
    "name": "Kepler-22b",
    "discovery_date": "2011-12-05",
    "mass": 2.4,
    "radius": 2.4,
    "orbital_period": 289.9,
    "distance_from_earth": 600
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Exoplanet created successfully:", response.json())
else:
    print("Failed to create exoplanet:", response.status_code, response.text)