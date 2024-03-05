# Previsão de Casos de COVID-19 em Botucatu - SP

## Visão Geral
Este projeto analisa os casos confirmados de COVID-19 em Botucatu - SP e usa um modelo ARIMA para prever a evolução desses casos. É utilizada a biblioteca `statsmodels` para ajustar o modelo aos dados históricos.

## Pré-requisitos
- Python 3.x
- Pandas
- Matplotlib
- Statsmodels

Instale as dependências via pip:

~~~CMD
pip install pandas matplotlib statsmodels
~~~

## Estrutura de Dados
O arquivo `Dados_COVID_Btu.csv` deve conter duas colunas:
1. Data (DD/MM/AAAA)
2. Casos confirmados

## Execução
Para executar a análise e visualizar as previsões, rode o script `previsao_covid.py`. O script divide os dados em treino e teste, ajusta o modelo ARIMA e plota a série temporal junto com as previsões.

## Modelo ARIMA
Os parâmetros do modelo ARIMA são inicialmente definidos como (5,1,2), mas podem ser ajustados conforme necessário.

## Visualização
O script gera um gráfico mostrando os casos confirmados e as previsões do modelo, facilitando a comparação visual entre os dados reais e as previsões.
