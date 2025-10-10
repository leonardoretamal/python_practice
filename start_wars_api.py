import requests


def fetch_data(option):
    url = f"https://swapi.mimo.dev/api/{option}/"
    data = []
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print(f"Successfully fetched {len(data)} entities")
    except requests.HTTPError as e:
        print(f"Error fetching data:{e}")
        return None
    return data


option = input("Ingresa una opcion (ej, 'people' o 'planets'): ").strip().lower()
data = fetch_data(option)

if data:
    for entity in data:
        print(entity["name"])
    else:
        print("No es posible descargar la informacion")
