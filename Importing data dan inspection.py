"""
Importlah dataset dari https://storage.googleapis.com/dqlab-dataset/data_retail.csv dan 
kemudian inspeksilah dataset tersebut dengan mencetak lima data teratas saja,
dan mencetak info dataset"""

import pandas as pd

df = pd.read_csv('data_retail.csv', sep=';')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info()) 
