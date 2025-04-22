import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

# Carregar os dados no DataFrame
df = pd.read_csv('ecommerce_estatistica.csv')

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Criar gráficos interativos com Plotly
fig_histograma = px.histogram(df, x='Preço', nbins=30, title="Distribuição dos Preços dos Produtos")
fig_dispersion = px.scatter(df, x='Nota', y='Preço', title="Relação entre Nota e Preço")

# Aqui a correção: só colunas numéricas pro heatmap
fig_heatmap = px.imshow(df.select_dtypes(include='number').corr(),
                        title="Mapa de Calor - Correlação Entre Variáveis")

fig_bar = px.bar(df.groupby('Marca')['Qtd_Vendidos'].sum().reset_index(),
                 x='Marca', y='Qtd_Vendidos', title="Total de Produtos Vendidos por Marca")

fig_pizza = px.pie(df, names='Marca', values='Qtd_Vendidos',
                   title="Distribuição das Vendas por Marca")

# Estrutura da aplicação Dash
app.layout = html.Div(children=[
    html.H1("Visualização de Dados - Ecommerce"),

    html.Div(children=[
        html.H3("Histograma de Preços"),
        dcc.Graph(figure=fig_histograma),

        html.H3("Gráfico de Dispersão"),
        dcc.Graph(figure=fig_dispersion),

        html.H3("Mapa de Calor"),
        dcc.Graph(figure=fig_heatmap),

        html.H3("Gráfico de Barra"),
        dcc.Graph(figure=fig_bar),

        html.H3("Gráfico de Pizza"),
        dcc.Graph(figure=fig_pizza)
    ])
])

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)