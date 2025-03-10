# Projeto de Regressão Linear

Este projeto implementa uma aplicação web simples para realizar previsões usando regressão linear. A aplicação é construída com Flask para o backend e HTML/CSS/JavaScript para o frontend.

## Estrutura do Projeto

- `app.py`: Contém o código do servidor Flask que lida com as requisições e realiza as previsões.
- `templates/index.html`: Contém o código HTML para a interface do usuário.
- `datas.csv`: Arquivo CSV contendo os dados de treinamento.

## Configuração do Ambiente

1. **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```

2. **Crie um ambiente virtual:**
    ```bash
    python -m venv my-venv
    ```

3. **Ative o ambiente virtual:**
    - No Windows:
        ```bash
        my-venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source my-venv/bin/activate
        ```

4. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Executando a Aplicação

1. **Inicie o servidor Flask:**
    ```bash
    python app.py
    ```

2. **Abra o navegador e acesse:**
    ```
    http://127.0.0.1:5000/
    ```

## Explicação do Código

### Backend (`app.py`)

- **Importações e Configuração:**
    ```python
    from flask import Flask, render_template, request, jsonify
    import numpy as np
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import matplotlib.pyplot as plt

    # Carrega a base de dados
    base = pd.read_csv('C:/Users/hugot/OneDrive/Documentos/Projetos/ADS-1/py_regressao/datas.csv')

    app = Flask(__name__)
    ```

- **Treinamento do Modelo:**
    ```python
    # Dados de treinamento
    X_train = np.array(base["TIME OCC"].head(2000)).reshape(-1, 1)
    y_train = np.array(base["Rpt Dist No"].head(2000))

    # Criar e treinar o modelo de regressão linear
    model = LinearRegression()
    model.fit(X_train, y_train)
    ```

- **Rotas do Flask:**
    ```python
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        X_test = np.array(data['input']).reshape(-1, 1)
        y_pred = model.predict(X_test)

        if X_test > X_train.max():
            x_range = np.linspace(X_train.min(), X_test).reshape(-1, 1)
        else:
            x_range = np.linspace(X_train.min(), X_train.max()).reshape(-1, 1)
        y_range = model.predict(x_range)

        plt.figure()
        plt.scatter(X_train, y_train, label='Dados de treinamento')
        plt.plot(x_range, y_range, "b-", label='Linha de Previsão')
        plt.scatter(X_test, y_pred, label='Previsão')
        plt.legend()
        plt.show()

        return jsonify({'prediction': y_pred.tolist()})

    if __name__ == '__main__':
        app.run(debug=True)
    ```

### Frontend (`templates/index.html`)

- **Estrutura HTML:**
    ```html
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Regressão Linear</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    </head>
    <body class="bg-gray-100 flex items-center justify-center h-screen">
        <div class="bg-white p-8 rounded-lg shadow-md w-96">
            <h1 class="text-2xl font-bold mb-4 text-center">Regressão Linear</h1>
            <form id="regressionForm" class="mb-4">
                <label for="input" class="block text-gray-700 mb-2">Digite o valor para previsão:</label>
                <input type="number" id="input" name="input" class="border border-gray-300 rounded-md p-2 w-full mb-4" required>
                <button type="submit" class="bg-blue-500 text-white rounded-md p-2 w-full hover:bg-blue-600">Prever</button>
            </form>
            <div id="result" class="text-center text-lg text-gray-800"></div>
        </div>

        <script>
            document.getElementById('regressionForm').addEventListener('submit', function(e) {
                e.preventDefault();
                const inputValue = parseFloat(document.getElementById('input').value);
                const inputData = { input: inputValue };

                fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(inputData)
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerHTML = `Previsão: ${data.prediction}`;
                });
            });
        </script>
    </body>
    </html>
    ```

## Licença

Este projeto está licenciado sob os termos da licença MIT.

> **Nota:** Essa documentação foi gerada automaticamente pelo GitHub Copilot usando o *GPT-4o*.