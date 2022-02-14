"""
Setelah semuanya lancar, langkah berikutnya adalah membuat visualisasi data berupa trend of customer acquisition by year dengan meggunakan bar chart. 
Untuk itu buatlah feature/kolom tambahan yang merupakan tahun dari First_Transaction dan tahun dari Last_Transaction masing-masingnya dengan nama 
Year_First_Transaction dan Year_Last_Transaction sebelum melakukan visualisasi.
"""

import matplotlib.pyplot as plt

# Kolom tahun transaksi pertama
df['Year_First_Transaction'] = df['First_Transaction'].dt.year
# Kolom tahun transaksi terakhir
df['Year_Last_Transaction'] = df['Last_Transaction'].dt.year

df_year = df.groupby(['Year_First_Transaction'])['Customer_ID'].count() 
df_year.plot(x='Year_First_Transaction', 
             y='Customer_ID', 
             kind='bar', 
             title='Graph of Customer Acquisition')
plt.xlabel('Year First Transaction')
plt.ylabel('Number of Customer')
plt.tight_layout()
# plt.savefig("GraphCustomerbyYear", format="png")
plt.show()
