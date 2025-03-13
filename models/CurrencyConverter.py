import sys

import requests
from views.View import View


class CurrencyConverter:
    def __init__(self):
        self.api_key = "fc9ac088c3d0fbd906fb84ae"
        self.base_url = "https://v6.exchangerate-api.com/v6/"
        self.rates = {}
        self.fetch_rates("EUR") #Tõmbab kursid ja kursside algväärtus on EUR

    def fetch_rates(self, base_currency):
        """Tõmbab APIga valuuta kursid ja salvestab need"""
        try:
            url = f'{self.base_url}{self.api_key}/latest/{base_currency}'
            response = requests.get(url)

            if response.status_code == 200: #Kontrollime, kas url vastab
                data = response.json()
                if data.get("result") == "success" and "conversion_rates" in data: #Kontrollime, kas data hulgas on vajalik ja tulemus õige
                    self.rates = data.get("conversion_rates") #Salvestab valuutakursid
                    return True
                else:
                    View.show_message('Viga valuutakursside andmete laadimisel. Kontrolli andmete nimetusi.')
                    sys.exit(1)
            else:
                View.show_message(f'Viga API aadressis. Staatusekood : {response.status_code}')
                sys.exit(1)
        except Exception as e:
            View.show_message(f'Tõrge API päringus: {e}')
            sys.exit(1)

    def get_user_input(self, user_input):
        try:
            user_input = float(user_input) * 2
            print(user_input)
        except ValueError:
            View.show_message('Sisesta korrektne arv.')