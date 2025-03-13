import pandas as pd 

# criar um datafrsme 

marketing = pd.read_csv('marketing.csv', delimiter=',')

print(marketing.head(5))

# Verifique o tipo de dado da coluna is_retained
print(marketing['is_retained'].dtype)

# Converta is_retained para booleano
marketing['is_retained'] = marketing['is_retained'].astype('bool')

# Verifique o tipo de dado da coluna is_retained
print(marketing['is_retained'].dtype) 