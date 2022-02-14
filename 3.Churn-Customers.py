""""
Churn customers
Cara untuk mengetahui pembeli termasuk dalam kategori churn atau tidak. 
Tentunya perlu mengetahui kapan terakhir data tersebut diperbaharui. 
Kemudian kategorikan pembeli yang berstatus churn atau tidak dengan boolean.
"""
# Pengecekan transaksi terakhir dalam dataset
print('Transaksi terakhir')
print(max(df['Last_Transaction'])) 

# Klasifikasikan customer yang berstatus churn atau tidak dengan boolean
df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True 
df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False 

print('Lima data teratas setelah dikategorikan:')
print(df.head())

print('\nInfo dataset setelah dikategorikan:')
print(df.info())
