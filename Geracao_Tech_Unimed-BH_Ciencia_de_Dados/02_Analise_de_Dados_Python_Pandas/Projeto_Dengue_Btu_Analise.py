import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
arquivo_dengue_btu = "Dengue_Botucatu_SP.csv"
df = pd.read_csv(arquivo_dengue_btu)

# Convertendo a coluna 'Data' para o formato datetime
df["Data"] = pd.to_datetime(df["Data"], dayfirst=True)

# Ordenando o DataFrame pela coluna 'Data'
df = df.sort_values(by="Data")

# Criando o gráfico de linhas para os casos confirmados
plt.figure(figsize=(10, 6)) # Configura o tamanho do gráfico
plt.plot(df["Data"], df["Total de confirmados"], marker='o', linestyle='-', color='b')

plt.title('Evolução dos Casos Confirmados de Dengue em Botucatu - SP')
plt.xlabel('Data')
plt.ylabel('Total de Casos Confirmados')
plt.xticks(rotation=45) # Rotaciona as datas no eixo x para melhor visualização
plt.tight_layout() # Ajusta automaticamente os parâmetros do subplot para o gráfico caber na figura

plt.show()