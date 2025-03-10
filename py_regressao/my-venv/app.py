from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carrega a base de dados
base = pd.read_csv('C:/Users/hugot/OneDrive/Documentos/Projetos/ADS-1/py_regressao/datas.csv')

app = Flask(__name__)

# Dados de treinamento
X_train = np.array(base["TIME OCC"].head(2000)).reshape(-1, 1)  # Variável de entrada (reshape para uma matriz 2D) com os 50 primeiros valores
y_train = np.array(base["Rpt Dist No"].head(2000))  # Variável de saída com os 50 primeiros valores

# Criar e treinar o modelo de regressão linear
model = LinearRegression() # Cria o modelo de regressão linear
model.fit(X_train, y_train) #  Treina o modelo com os dados de treinamento | fit() == trinar a rede neural

@app.route('/') # Define um rota, a rota raiz | O Flask que faz isso
def index():
    return render_template('index.html') # Renderiza o template HTML, que precisa estar na pasta templates

@app.route('/predict', methods=['POST']) # Rota POST para fazer a previsão
def predict():
    data = request.get_json() # Recupera os dados enviados pelo formulário
    X_test = np.array(data['input']).reshape(-1, 1) # Armazena e transforma os dados num array 2D

    # Com o modelo treinado usando fit(), podemos fazer previsões com o método predict()
    y_pred = model.predict(X_test) # Faz a previsão com o modelo treinado
    if X_test > X_train.max():
        x_range = np.linspace(X_train.min(), X_test).reshape(-1, 1)
        # np.concatenate((X_train, X_test))
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