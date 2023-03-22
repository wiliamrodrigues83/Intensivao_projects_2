# Análise de Dados

import pandas as pd
import plotly.express as px


tabela = pd.read_csv(r'C:/Users/UK/IT/Python/HASHTAG/intensivao_hashtag/Aula_2/clientes.csv', encoding="latin", sep=";")
tabela = tabela.drop('Unnamed: 8', axis = 'columns')
#print(tabela)

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors = "coerce")
tabela = tabela.dropna()
#print(tabela.info())

#print(tabela.describe())




for column in tabela.columns:
    grafico = px.histogram(tabela, x=column, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()



