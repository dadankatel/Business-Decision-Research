"""
Transaction by year

Selanjutnya memvisualisasi kondisi trend jumlah transaksi setiap tahunnya dengan bar chart.
"""

plt.clf()
df_year = df.groupby(['Year_First_Transaction'])['Count_Transaction'].sum() 
df_year.plot(x='Year_First_Transaction', 
             y='Count_Transaction', 
             kind='bar', 
             title='Graph of Transaction Customer')
plt.xlabel('Year First Transaction')
plt.ylabel('Number of Transaction')
plt.tight_layout()
# plt.savefig("GraphofTransaction", format='png')
plt.show()
