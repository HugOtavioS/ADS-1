from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

base = pd.read_csv('C:/Users/hugot/Documents/Projetos/ADS-1/py_regressao/bets.csv')
# print(np.array(base[""]))

app = Flask(__name__)

# Dados de treinamento
X_train = np.array(base["home_team_goal"]).reshape(-1, 1)  # Variável de entrada (reshape para uma matriz 2D)
y_train = np.array(base["away_team_goal"])  # Variável de saída

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    X_test = np.array(data['input']).reshape(-1, 1)  # Variável de entrada para teste
    y_pred = model.predict(X_test)
    return jsonify({'prediction': y_pred.tolist()})

if __name__ == '__main__':
    app.run(debug=True)