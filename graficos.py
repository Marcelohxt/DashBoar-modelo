import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria ,df_vendedores

# Gráfico de mapa por estado
grafico_map_estado = px.scatter_geo(
    df_rec_estado, 
    lat='lat',  # Latitude dos pontos no gráfico
    lon='lon',  # Longitude dos pontos no gráfico
    scope='south america',  # Escopo do mapa (nesse caso, América do Sul)
    size='Preço',  # Tamanho dos pontos no gráfico, baseado na coluna 'Preço'
    template='seaborn',  # Estilo do gráfico
    hover_name='Local da compra',  # Nome exibido ao passar o mouse sobre os pontos
    hover_data={'lat': False, 'lon': False},  # Dados exibidos ao passar o mouse
    title='Receita Por Estado'  # Título do gráfico
)

# Gráfico de receita mensal
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mes',  # Eixo x do gráfico, representando o mês
    y='Preço',  # Eixo y do gráfico, representando o preço
    markers=True,  # Exibir marcadores no gráfico
    range_y=(0, df_rec_mensal['Preço'].max()),  # Intervalo do eixo y (preço máximo)
    color='Ano',  # Colorir linhas com base no ano
    line_dash='Ano',  # Estilo das linhas
    title='Receita Mensal'  # Título do gráfico
)

# Ajuste do layout do gráfico de receita mensal
grafico_rec_mensal.update_layout(yaxis_title='Receita')  # Título do eixo y


# Gráfico de barras de receita por estado
grafico_rec_estado = px.bar(
    df_rec_estado.head(7),  # Usando os 7 primeiros estados com maior receita
    x='Local da compra',  # Usando o nome correto da coluna para o eixo x
    y='Preço',  # Representando a receita no eixo y
    text_auto=True,  # Exibir valores dos dados automaticamente
    title='Top Receita Por Estados'  # Título do gráfico
)


# grafico de categoria

grafico_rec_categoria= px.bar(
    df_rec_categoria.head(7),
    text_auto= True,
    title= 'Top 7 categorias com Maior Receita'

)


# Gráfico de barra para os top 7 vendedores por receita
grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),  # Ordena os dados pela coluna 'sum' em ordem decrescente e seleciona os 7 primeiros
    x='sum',  # Define os valores da coluna 'sum' como o eixo x
    y=df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,  # Define os índices dos dados como o eixo y
    text_auto=True,  # Habilita a exibição automática de rótulos nos gráficos de barra
    title='Top 7 vendedores por Receita'  # Define o título do gráfico
)


grafico_vendas_vendedores = px.bar(
      df_vendedores[['count']].sort_values('count', ascending=False).head(7),
      x = 'count',
      y = df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
      text_auto=True,
      title= 'Top 7 Vendas De Vendedores'

)
