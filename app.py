import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from dash import Dash, html, dcc
import unicodedata


# === 1. Ler os dados e padronizar colunas ===
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


df = pd.read_csv(r"C:\Users\Gabriel Estudo\Downloads\ecommerce_estatistica.csv")
df.columns = [remover_acentos(col).strip().lower() for col in df.columns]

# === 2. Gráficos ===

# Histograma
fig_hist = px.histogram(df, x='preco', nbins=30, title='Distribuição de Preços')

# Dispersão
fig_scatter = px.scatter(df, x='preco', y='nota', title='Dispersão: Preço vs Nota')

# Mapa de Calor
# Mapa de Calor com px.imshow
corr = df.corr(numeric_only=True)
fig_heatmap = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale='Viridis',
    title='Mapa de Calor das Correlações'
)
fig_heatmap.update_layout(width=800, height=800)
# Barras - Gênero
df_genero = df['genero'].value_counts().reset_index()
df_genero.columns = ['genero', 'count']

fig_bar = px.bar(df_genero,
                 x='genero', y='count',
                 title='Distribuição por Gênero',
                 labels={'genero': 'Gênero', 'count': 'Contagem'})

# Pizza - Top 5 Materiais + "Outros"
materiais = df['material'].value_counts()

top5 = materiais.head(5)
outros = materiais.iloc[5:].sum()

# Concatena Top 5 + Outros
materiais_ajustados = pd.concat([top5, pd.Series({'Outros': outros})])

# Gráfico de pizza
fig_pizza = px.pie(
    values=materiais_ajustados.values,
    names=materiais_ajustados.index,
    title='Top 5 Materiais + Outros'
)

# Ajustar tamanho do gráfico
fig_pizza.update_layout(width=750, height=750)

# Criar lista dos materiais que foram agrupados como "Outros"
outros_materiais = materiais.iloc[5:].index.tolist()

# Densidade
fig_density = ff.create_distplot(
    [df['preco'].dropna()],
    group_labels=['Preço'],
    show_hist=False
)

fig_density.update_layout(
    title_text='Distribuição de Densidade de Preços',
)


# Regressão
fig_reg = px.scatter(df, x='preco', y='qtd_vendidos_cod', trendline='ols',
                     title='Regressão: Preço vs Qtd Vendidos Codificados')

# === 3. App Dash ===
app = Dash(__name__)
app.title = "Visualização E-commerce"

app.layout = html.Div(children=[
    html.H1('Análise Estatística de E-commerce', style={'textAlign': 'center'}),

    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_scatter),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_heatmap)
        ], style={'flex': '1'}),

        html.Div([
            html.H4("Como interpretar o Mapa de Calor", style={'marginBottom': '10px'}),
            html.P("Este gráfico mostra a correlação entre variáveis numéricas."),
            html.Ul([
                html.Li("Valores próximos de 1: correlação forte e positiva."),
                html.Li("Valores próximos de -1: correlação forte e negativa."),
                html.Li("Valores próximos de 0: pouca ou nenhuma correlação."),
                html.Li("As cores representam a intensidade da correlação."),
            ]),
            html.P("Por exemplo, se 'preço' e 'qtd_vendidos_cod' tiverem correlação negativa, "
                   "isso indica que à medida que o preço aumenta, a quantidade vendida tende a diminuir.")
        ], style={
            'flex': '1',
            'padding': '20px',
            'maxWidth': '400px',
            'fontSize': '15px'
        })
    ], style={'display': 'flex', 'gap': '30px', 'margin': '40px 0'}),
    dcc.Graph(figure=fig_bar),
    html.Div([
        html.Div([
            dcc.Graph(figure=fig_pizza)
        ], style={'flex': '1'}),

        html.Div([
            html.P("Materiais agrupados como 'Outros':", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            html.Ul([html.Li(material) for material in outros_materiais])
        ], style={
            'flex': '1',
            'padding': '20px',
            'overflowY': 'auto',
            'maxHeight': '700px',
            'borderLeft': '1px solid #ccc'
        })
    ], style={'display': 'flex', 'gap': '20px'}),

    html.Div([
        dcc.Graph(figure=fig_density),

        html.Div([
            html.H4("Como interpretar este gráfico de densidade", style={'marginBottom': '10px'}),
            html.P("Este gráfico mostra a distribuição contínua dos preços dos produtos."),
            html.Ul([
                html.Li("Picos representam faixas de preço com maior concentração de produtos."),
                html.Li("Não mostra frequência exata, mas a tendência geral da distribuição."),
                html.Li("É útil para identificar se os preços estão concentrados, dispersos ou com múltiplos picos."),
            ]),
            html.P(
                "Neste caso, observe onde a curva atinge o valor mais alto — isso indica o intervalo de preço mais comum.")
        ], style={
            'marginTop': '10px',
            'textAlign': 'left',
            'fontSize': '15px',
            'maxWidth': '700px',
            'margin': '0 auto'
        })
    ]),
    html.Div([
        dcc.Graph(figure=fig_reg),

        html.Div([
            html.H4("Como interpretar este gráfico de regressão", style={'marginBottom': '10px'}),
            html.P("Este gráfico mostra como o preço dos produtos se relaciona com a quantidade vendida (codificada)."),
            html.Ul([
                html.Li("Cada ponto representa um produto individual."),
                html.Li("A linha azul é a linha de tendência (regressão linear)."),
                html.Li(
                    "Se a linha desce da esquerda para a direita, indica que preços maiores tendem a vender menos."),
                html.Li("Se sobe, indica que produtos mais caros vendem mais."),
                html.Li("A dispersão dos pontos em torno da linha mostra a força dessa relação."),
            ]),
            html.P("Este tipo de gráfico ajuda a entender se há alguma tendência geral entre preço e vendas.")
        ], style={
            'marginTop': '10px',
            'textAlign': 'left',
            'fontSize': '15px',
            'maxWidth': '800px',
            'margin': '0 auto'
        })
    ]),

])

if __name__ == '__main__':
    app.run(debug=True)

