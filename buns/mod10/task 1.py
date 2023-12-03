import requests
import json


def data_in_json(url):
    response = requests.get(url)
    return response.json()


def get_ship_info(ship):
    ship_url = f'https://swapi.dev/api/starships/?search={ship}'
    ship_info = data_in_json(ship_url)
    ship = ship_info['results'][0]
    pilots_info = []

    for pilot_url in ship['pilots']:
        pilot_info = data_in_json(pilot_url)

        pilot_info = {
            'name': pilot_info['name'],
            'height': pilot_info['height'],
            'mass': pilot_info['mass'],
            'homeworld': data_in_json(pilot_info['homeworld'])['name'],
            'homeworld_url': pilot_info['homeworld']
        }

        pilots_info.append(pilot_info)

    result = {
        'ship_name': ship['name'],
        'starship_class': ship['starship_class'],
        'max_atmosphering_speed': ship['max_atmosphering_speed'],
        'pilots': pilots_info
    }

    print(json.dumps(result, indent=2))

    with open('Millennium_Falcon_ship_info.json', 'w') as file:
        json.dump(result, file, indent=2)


ship_name = 'Millennium Falcon'
get_ship_info(ship_name)
