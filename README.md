Really simple. For using you need:

    pip install requests pandas openpyxl


Then you insert your API key in:

    # Clave API de Steam
    api_key = 'YOUR_STEAM_ID'


And add the necessary user ids and put the names you like for each user in:

    # REPLACE THE VALUES IN STEAM_IDS WITH YOUR IDS AND NAMES DESIRED
    def main():
        steam_ids = {'ID_1': 'USER_1', 'ID_2': 'USER_2', 'ID_3': 'USER_3'}
