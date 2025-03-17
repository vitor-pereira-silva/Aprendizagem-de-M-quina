import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# criar um datafrsme 

marketing = pd.read_csv('marketing.csv', delimiter=',')

#Imprima as primeira 5 linhas 
print(marketing.head(5))

#Imprima um resumo estatístico de todas as colunas 
print(marketing.describe(include='all'))

#Imprima tipos de dados das colunas e a quantidade de valores não-nulos por coluna
print(marketing['converted'].head(5))

#conversao 
marketing['converted'] = marketing['converted'].astype('bool')
print(marketing['converted'].dtype)

#Criando novas colunas do tipo Bool
marketing['is_house_ads'] = np.where(marketing['marketing_channel'] == 'House Ads', True, False)
print(marketing.is_house_ads.head(3))

#Mapeando valores às colunas existentes
channel_dict = { "House Ads": 1, "Instagram": 2, "Facebook": 3, "Email": 4, "Push": 5}
marketing['channel_code'] =marketing['marketing_channel'].map(channel_dict)
print(marketing['channel_code'].head(3))

#Colunas do tipo Data

#ler colunas de data usando parse_dates
marketing = pd.read_csv('marketing.csv', parse_dates=['date_served', 'date_subscribed', 'date_canceled'])
print(marketing[['date_served', 'date_subscribed', 'date_canceled']])

# coverter coluna ja exisatente em coluna datetime
marketing['date_served'] = pd.to_datetime(marketing['date_served'])
print(marketing['date_served'] )

#extrai o dia da semana da coluna
marketing['day_served']= marketing["date_served"].dt.dayofweek
print(marketing['day_served'])

# Atualizar o tipo de dados de uma coluna 
marketing['is_retained']= marketing["is_retained"]
print(marketing['is_retained'].dtype)

# Converta is_retained para booleano
marketing['is_retained']=marketing['is_retained'].astype('bool')
print(marketing['is_retained'].dtype)

#add nova coluna 
import pandas as pd

# Criando um DataFrame de exemplo
data = {'subscribing_channel': ['House Ads', 'Instagram', 'Facebook', 'Email', 'Push']}
marketing = pd.DataFrame(data)

# Criando o dicionário de mapeamento 
channel_dict = {
    "House Ads": 1,
    "Instagram": 2,  
    "Facebook": 3, 
    "Email": 4,
    "Push": 5  
}

# Aplicando o mapeamento 
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# Exibindo o resultado
print(marketing)



# Import marketing.csv with date columns
marketing = pd.read_csv('marketing.csv', parse_dates=['date_served', 'date_subscribed', 'date_canceled'])

# Add a DoW (Day of Week) column
marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek

print(marketing)

# Agregar usuários únicos que vêm através de anúncios por data
daily_users = marketing.groupby(['date_served'])['user_id'].nunique()

# Exibir o resultado
print(daily_users.head(3))

import matplotlib.pyplot as plt

# Plota o gráfico
daily_users.plot()

# Adiciona anotações ao gráfico
plt.title('Daily number of users who see ads')
plt.xlabel('Date')
plt.ylabel('Number of users')
plt.xticks(rotation= 45) 
plt.show()
