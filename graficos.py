import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


# Carregar os dados do arquivo CSV
dados = pd.read_csv('cert_2010-2019.csv', delimiter=';')

# Filtrar os dados removendo os anos de 2010 a 2014
dados_filtrados = dados[(dados['Ano'] >= 2015)]

# Agrupar os dados filtrados por ano e calcular a soma das colunas
dados_agrupados = dados_filtrados.groupby('Ano').sum()

# Selecionar as colunas relevantes
colunas = ['Worm', 'Invasao', 'Web', 'Scan', 'Fraude', 'Outros']

# Configurar a figura e os subplots
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# ------------------------
# Gráfico 1: Gráfico de Barras
# ------------------------

# Transpor o DataFrame para que as colunas se tornem as linhas
dados_agrupados_transpose = dados_agrupados[colunas].transpose()

# Plotar o gráfico de barras no primeiro subplot
dados_agrupados_transpose.plot(kind='bar', ax=axs[0])
axs[0].set_ylabel('Número de incidentes')
axs[0].set_title('Incidentes entre os anos de 2015 a 2019', fontsize=8)
axs[0].tick_params(axis='y', labelsize=6)  # Diminui o tamanho da fonte do eixo Y

# ------------------------
# Gráfico 2: Gráfico de Setores
# ------------------------

# Agrupar os dados por ano e encontrar o mês com maior número de incidentes em cada ano
meses_maiores_incidentes = dados_filtrados.groupby('Ano')['Total'].idxmax()

# Filtrar os dados apenas com os meses de maior número de incidentes em cada ano
meses_maior_incidente_df = dados_filtrados.loc[meses_maiores_incidentes, ['Ano', 'Mes', 'Total']]


# Plotar o gráfico de setores no segundo subplot
axs[1].pie(meses_maior_incidente_df['Total'], labels=meses_maior_incidente_df['Mes'] + ' ' + meses_maior_incidente_df['Ano'].astype(str), autopct='%1.1f%%')
axs[1].set_title('Meses com maiores incidentes entre os anos de 2015 a 2019', fontsize=8)

# ------------------------
# Gráfico 3: Treemap
# ------------------------

# Cria um treemap utilizando os dados filtrados
fig = px.treemap(dados_filtrados, path=['Ano', 'Mes'], values='Total', hover_data=['Worm', 'DOS', 'Invasao', 'Web', 'Scan', 'Fraude', 'Outros'])

# Exibir a figura
fig.show()


# Ajustar o espaçamento entre os subplots
plt.tight_layout(pad=2.0)

# Título principal para todos os gráficos
plt.suptitle('Incidentes de Segurança da Informação no Brasil entre 2015 a 2019', fontsize=12, y=1)


# Exibir a figura com os subplots
plt.show()
