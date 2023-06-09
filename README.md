## Currency Converter

Este é um aplicativo de conversão de moedas construído com o PySimpleGUI. Ele permite que os usuários convertam valores de uma moeda para outra com base nas taxas de câmbio obtidas de uma API.

![CurrencyNowpython](https://github.com/Yur3e/CurrencyNOW-Python/assets/88630655/96135c97-5c40-4ed5-80c2-ca01402bc2c8)


### Funcionalidades

- Entrada da moeda a converter, valor e moeda de conversão.
- Botão "Converter" para iniciar a conversão.
- Exibição do resultado da conversão ou mensagens de erro na tabela abaixo.

### Dependências

- `requests`
- `PySimpleGUI`

### Instalação

Certifique-se de ter o Python e o pip instalados em seu ambiente. Em seguida, instale as dependências executando o seguinte comando:

```shell
pip install requests PySimpleGUI
```

### Uso

1. Importe as bibliotecas `requests` e `PySimpleGUI`.
2. Defina a classe `CurrencyNowApp`.
3. No construtor `__init__`, crie o layout da interface gráfica com os campos de entrada e a tabela de saída.
4. Implemente o método `run` para iniciar o loop principal do aplicativo.
5. Dentro do loop, verifique o evento disparado pela interação do usuário.
   - Se o evento for o fechamento da janela, encerre o loop e finalize o aplicativo.
   - Se o evento for o clique no botão "Converter", obtenha os valores dos campos de entrada, realize a conversão e exiba o resultado ou uma mensagem de erro.
6. Implemente o método `get_exchange_rate` para obter a taxa de câmbio da API.
7. Implemente o método `show_result` para exibir o resultado da conversão na tabela de saída.
8. Implemente o método `show_error` para exibir mensagens de erro na tabela de saída.
9. Na condição `if __name__ == "__main__":`, crie uma instância da classe `CurrencyNowApp` e execute o método `run` para iniciar o aplicativo.

### Exemplo

```python
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
        data = response.json

()
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
```

### Execução

Execute o script Python e a janela do aplicativo "Currency Converter" será aberta. Preencha os campos de entrada com a moeda a converter, o valor e a moeda de conversão. Em seguida, clique no botão "Converter" para ver o resultado da conversão exibido na tabela abaixo. Se ocorrer um erro na obtenção da taxa de câmbio, uma mensagem de erro será exibida na tabela.

```shell
python currency_converter.py
```
