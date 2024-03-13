import pandas as pd


############### Caminho das Bases ###############
goals_scorers = 'goalscorers.csv'
results = 'results.csv'
shootouts = 'shootouts'


############### Lendo as Bases ###############

df_1 = pd.read_csv(goals_scorers, encoding='UTF-8')
df_2 = pd.read_csv(results, encoding='UTF-8')
df_3 = pd.read_csv(shootouts, encoding='UTF-8')

############### Tratamento dos Dados ###############


df_1['date'] = pd.to_datetime(df_1['date'])
df_1['date'] = df_1['date'].dt.strftime('%d/%m/%Y')
print(df_1.info())
print(df_1.head())