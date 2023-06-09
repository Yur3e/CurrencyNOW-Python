import requests
import PySimpleGUI as sg

class CurrencyNowApp:
    def __init__(self):
        self.layout = [
            [sg.Text("Moeda a converter:"), sg.Input(key="-CURRENCY-")],
            [sg.Text("Valor:"), sg.Input(key="-VALUE-")],
            [sg.Text("Converter para:"), sg.Input(key="-CONVERT_TO-")],
            [sg.Button("Converter", key="-CONVERT_BUTTON-")],
            [sg.Output(size=(60, 10), key="-OUTPUT-")]
        ]
        self.window = sg.Window("Currency Converter", self.layout)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == "-CONVERT_BUTTON-":
                currency = values["-CURRENCY-"].upper()
                value = float(values["-VALUE-"])
                convert_to = values["-CONVERT_TO-"].upper()
                try:
                    exchange_rate = self.get_exchange_rate(currency, convert_to)
                    converted_value = value * exchange_rate
                    self.show_result(currency, value, convert_to, converted_value)
                except requests.exceptions.RequestException:
                    self.show_error("Erro ao obter a cotação. Verifique sua conexão com a internet.")

    def get_exchange_rate(self, base_currency, target_currency):
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        rates = data["rates"]
        return rates[target_currency]

    def show_result(self, base_currency, value, target_currency, converted_value):
        result_text = f"Você selecionou {base_currency} no valor de {value} para converter em {target_currency} = {converted_value:.2f}"
        print(result_text)

    def show_error(self, error_message):
        print(error_message)

if __name__ == "__main__":
    app = CurrencyNowApp()
    app.run()
