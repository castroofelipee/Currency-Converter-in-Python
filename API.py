import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest"

    def get_exchange_rates(self):
        url = f"{self.base_url}?apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data["rates"]

    def convert_currency(self, amount, from_currency, to_currency):
        exchange_rates = self.get_exchange_rates()

        if from_currency != "USD":
            amount_in_usd = amount / exchange_rates[from_currency]
        else:
            amount_in_usd = amount

        converted_amount = amount_in_usd * exchange_rates[to_currency]
        return converted_amount


if __name__ == "__main__":
    api_key = '**************'
    converter = CurrencyConverter(api_key)

    
    print("Taxas de câmbio disponíveis:")
    rates = converter.get_exchange_rates()
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")

   
    amount_to_convert = float(input("Digite o valor a ser convertido: "))
    from_currency = input("Digite a moeda de origem (código de 3 letras): ").upper()
    to_currency = input("Digite a moeda de destino (código de 3 letras): ").upper()

    converted_amount = converter.convert_currency(amount_to_convert, from_currency, to_currency)
    print(f"{amount_to_convert} {from_currency} é equivalente a {converted_amount} {to_currency}")
