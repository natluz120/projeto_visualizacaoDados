import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv('ecommerce_estatistica.csv')

# Exibir as primeiras linhas do DataFrame para análise
print(df.head())

# Criar um gráfico de histograma para a variável "Preço"
plt.figure(figsize=(8, 5))
sns.histplot(df['Preço'], bins=30, kde=True, color='blue')
plt.title('Distribuição dos Preços dos Produtos')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

# Criar um gráfico de dispersão entre "Preço" e "Nota"
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Nota'], y=df['Preço'], alpha=0.7)
plt.title('Relação entre Nota e Preço dos Produtos')
plt.xlabel('Nota Média')
plt.ylabel('Preço')
plt.show()

# Criar um mapa de calor para correlação entre variáveis numéricas
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor - Correlação Entre Variáveis')
plt.show()

# Criar um gráfico de barras para visualizar a quantidade vendida por marca
plt.figure(figsize=(10, 5))
df.groupby('Marca')['Qtd_Vendidos'].sum().sort_values(ascending=False).plot(kind='bar', color='green')
plt.title('Total de Produtos Vendidos por Marca')
plt.xlabel('Marca')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()

# Criar um gráfico de pizza para representar a distribuição de avaliações
plt.figure(figsize=(8, 8))
df['Nota'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red', 'blue', 'green', 'yellow', 'purple'])
plt.title('Distribuição das Notas dos Produtos')
plt.ylabel('')
plt.show()

# Criar um gráfico de densidade para a variável "Preço"
plt.figure(figsize=(8, 5))
sns.kdeplot(df['Preço'], fill=True, color='purple')
plt.title('Densidade dos Preços dos Produtos')
plt.xlabel('Preço')
plt.show()

# Criar um gráfico de regressão para visualizar a relação entre "Preço" e "Qtd_Vendidos"
plt.figure(figsize=(8, 5))
sns.regplot(x=df['Preço'], y=df['Qtd_Vendidos'], scatter_kws={"alpha":0.5})
plt.title('Regressão entre Preço e Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()
