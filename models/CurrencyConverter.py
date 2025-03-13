import sys

import requests
from views.View import View


class CurrencyConverter:
    def __init__(self):
        self.api_key = "Insert API Key Here"
        self.base_url = "https://v6.exchangerate-api.com/v6/"
        self.rates = {}
        self.base_currency = "EUR" #Kursside algväärtus on EUR
        self.fetch_rates() #Tõmbab kursid
        self.result = None
        self.amount = None

    def fetch_rates(self):
        """Tõmbab APIga valuuta kursid ja salvestab need"""
        try:
            url = f'{self.base_url}{self.api_key}/latest/{self.base_currency}'
            response = requests.get(url)

            if response.status_code == 200: #Kontrollime, kas url vastab
                data = response.json()
                if data.get("result") == "success" and "conversion_rates" in data: #Kontrollime, kas data hulgas on vajalik ja tulemus õige
                    self.rates = data.get("conversion_rates") #Salvestab valuutakursid
                else:
                    View.show_message('Viga valuutakursside andmete laadimisel. Kontrolli andmete nimetusi.')
                    sys.exit(1)
            else:
                View.show_message(f'Viga API aadressis. Staatusekood : {response.status_code}')
                sys.exit(1)
        except Exception as e:
            View.show_message(f'Tõrge API päringus: {e}')
            sys.exit(1)

    def convert_currency(self, cfrom, cto):
        """Konverteerib vastavalt valitud valuutale"""
        if cfrom != self.base_currency: #Kui alus valuuta pole hetkel päringu valuuta, käivitab vajaliku päringu
            self.base_currency = cfrom
            self.fetch_rates()
        if cto in self.rates: #kontrollib, kas siht valuuta on andmete hulgas
            self.result = self.amount * self.rates[cto] #Korrutab summa kursiga
        else:
            View.show_message(f'Valuuta {cto} kurssi ei leitud.!')
            self.result = 0
        return self.result

    def get_user_input(self, user_input):
        """Entry boxi andmete kontroll"""
        try:
            self.amount = float(user_input) #Salvestame amount, peab saama olla float
        except ValueError:
            View.show_message('Sisesta korrektne arv.')
            self.amount = 0
        return self.amount