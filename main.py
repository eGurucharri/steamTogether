import requests
import pandas as pd

# Clave API de Steam
api_key = 'YOUR_STEAM_ID'


def obtener_lista_juegos():
    """Obtiene la lista completa de juegos en Steam."""
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(url)
    data = response.json()
    return {int(app['appid']): app['name'] for app in data['applist']['apps']}


def obtener_juegos(steam_id, juegos_dict):
    """Obtiene la lista de juegos de un usuario de Steam."""
    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json&include_appinfo=true"
    response = requests.get(url)
    data = response.json()
    juegos = []
    for item in data['response']['games']:
        appid = item['appid']
        nombre = juegos_dict.get(appid, 'Unknown Game')
        juegos.append((appid, nombre))
    return juegos


# REPLACE THE VALUES IN STEAM_IDS WITH YOUR IDS AND NAMES DESIRED
def main():
    steam_ids = {'ID_1': 'USER_1', 'ID_2': 'USER_2', 'ID_3': 'USER_3'}
    juegos_dict = obtener_lista_juegos()
    juegos_usuarios = {}
    for steam_id in steam_ids:
        juegos_usuarios[steam_id] = obtener_juegos(steam_id, juegos_dict)
    all_games = pd.DataFrame([
        {'Usuario': steam_ids[steam_id], 'SteamID': steam_id, 'AppID': game[0], 'Nombre del juego': game[1]}
        for steam_id, games in juegos_usuarios.items()
        for game in games
    ])
    all_games['Usuarios con el juego'] = all_games.groupby('AppID')['Usuario'].transform(lambda x: ', '.join(x))
    all_games = all_games.drop_duplicates(subset=['AppID']).sort_values(by='Nombre del juego')[['Nombre del juego', 'Usuarios con el juego']]
    all_games.to_excel('juegos_steam.xlsx', index=False)


if __name__ == '__main__':
    main()
