from dataset import df 
import pandas as pd
import streamlit as st
import time



# Função para formatar números com um prefixo opcional
def format_number(value, prefix = ''):
    # Loop sobre unidades de milhar ('' para unidades de mil, 'mil' para milhões)
    for unit in ['', 'mil']:
        # Verifica se o valor é menor que 1000
        if value < 1000:
            # Retorna o valor formatado com duas casas decimais e a unidade atual
            return f'{prefix} {value:.2f}{unit}'
        # Divide o valor por 1000 para a próxima iteração (se houver)
        value /= 1000
    # Retorna o valor formatado em milhões se for maior ou igual a 1000
    return f'{prefix}{value:.2f} milhões'


# 1 DataFrame de receita por estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
    # Aqui estamos agrupando os dados do DataFrame `df` pela coluna 'Local da compra'
    # e calculando a soma dos valores da coluna 'Preço' para cada grupo.

df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)
    # Aqui estamos removendo duplicatas da coluna 'Local da compra' do DataFrame `df`
    # e selecionando as colunas 'Local da compra', 'lat' e 'lon' do DataFrame resultante.
    # Em seguida, mesclamos esse DataFrame com o DataFrame `df_rec_estado` calculado anteriormente,
    # usando a coluna 'Local da compra' como chave para a mesclagem.
    # Por fim, ordenamos o DataFrame resultante pelo valor da coluna 'Preço' em ordem decrescente.


# 2 DataFrame de receita mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
    # Aqui estamos definindo a coluna 'Data da Compra' como índice do DataFrame `df`
    # e agrupando os dados por mês ('M') usando o método `groupby`.
    # Em seguida, estamos calculando a soma dos valores da coluna 'Preço' para cada mês.

df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
    # Aqui estamos extraindo o ano da coluna 'Data da Compra' e armazenando-o na nova coluna 'Ano'.

df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
    # Aqui estamos extraindo o nome do mês da coluna 'Data da Compra' e armazenando-o na nova coluna 'Mes'.


# 3 DataFrame de receita por categoria
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
    # Aqui estamos agrupando os dados do DataFrame `df` pela coluna 'Categoria do Produto'
    # e calculando a soma dos valores da coluna 'Preço' para cada categoria.
    # Em seguida, estamos ordenando o DataFrame resultante pelo valor da coluna 'Preço' em ordem decrescente.

print(df_rec_categoria.head())
    # Aqui estamos imprimindo as primeiras linhas do DataFrame `df_rec_categoria`.

# 4 DataFrame Vendedores
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))



# funcao para converter arquivos csv

@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success('arquivo baixado com sucesso')