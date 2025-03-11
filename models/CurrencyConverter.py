class CurrencyConverter:

    def get_user_input(self, user_input):
        try:
            float(user_input)
            print(user_input)
        except ValueError as e:
            print(f'VIGA: {e}')