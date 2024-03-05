import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Carregamento dos dados
arquivo_dengue_btu = "Dados_COVID_Btu.csv"
df = pd.read_csv(arquivo_dengue_btu, encoding='ISO-8859-1', skiprows=2)

# Conversão da primeira coluna para datetime e a segunda coluna para numérico
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], dayfirst=True, errors='coerce')
df.iloc[:, 1] = pd.to_numeric(df.iloc[:, 1], errors='coerce')

# Ordenando o DataFrame pela data
df = df.sort_values(by=df.columns[0])

# Definindo a coluna de data como índice
df.set_index(df.columns[0], inplace=True)

# Selecionando apenas a coluna de casos confirmados para a modelagem
series = df.iloc[:, 0]

# Dividindo os dados em treino e teste
n = len(series)
train = series[:int(n*0.8)]
test = series[int(n*0.8):]

# Ajustando o modelo ARIMA
# Os parâmetros (p, d, q) devem ser ajustados conforme a sua série temporal
model = ARIMA(train, order=(5,1,2))  # Estes são valores hipotéticos
fitted_model = model.fit()

# Fazendo previsões
forecast = fitted_model.forecast(steps=len(test))

# Plotando os resultados da série temporal e a previsão
plt.figure(figsize=(10, 6))
plt.plot(train.index, train, label='Dados de Treino')
plt.plot(test.index, test, label='Dados Reais de Teste')
plt.plot(test.index, forecast, label='Previsão', color='red')
plt.title('Previsão da evolução dos casos confirmados de COVID-19 em Botucatu - SP')
plt.xlabel('Data')
plt.ylabel('Casos Confirmados')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()