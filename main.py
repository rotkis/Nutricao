import pandas as pd
columns_to_read = ['CODMUNNASC', 'IDADEMAE', 'ESCMAE', 'ESTCIVMAE', 'CONSULTAS']  # Liste apenas as colunas que você precisa
base_de_dados = pd.read_csv("https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/DN23OPEN.csv", sep=";", usecols=columns_to_read)
# Carregar o CSV para análise
base_de_dados = pd.read_csv("https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SIM/DN23OPEN.csv", sep=";",low_memory=False)

# Selecionar colunas
selected_columns = ['CODMUNNASC', 'IDADEMAE', 'ESCMAE', 'ESTCIVMAE', 'CONSULTAS']

# Filtrar os dados
filtered_data = base_de_dados[selected_columns]

#Filtrar os dados de Limeira
df = (filtered_data[filtered_data['CODMUNNASC'] == 352690])

print(df)
df.shape
df.info()