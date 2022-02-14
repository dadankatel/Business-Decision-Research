"""
Selanjutnya akan melakukan visualisasi dari distribusi kategorisasi count transaction. 
Kategorisasi ini dilakukan dengan mengelompokkan jumlah transaksi seperti yang diperlihatkan oleh tabel berikut: 
Rentang jumlah transaksi		Kategori 
			s/d 1 										1 
			2 s/d 3 								 2 - 3 
			4 s/d 6									 4 - 6 
			7 s/d 10 								 7 - 10
			> 10											> 10
"""
plt.clf()
# Kategorisasi jumlah transaksi
def func(row):
    if row['Count_Transaction'] == 1:
        val = '1'
    elif (row['Count_Transaction'] > 1 and row['Count_Transaction'] <= 3):
        val ='2 - 3'
    elif (row['Count_Transaction'] > 3 and row['Count_Transaction'] <= 6):
        val ='4 - 6'
    elif (row['Count_Transaction'] > 6 and row['Count_Transaction'] <= 10):
        val ='7 - 10'
    else:
        val ='> 10'
    return val
# Tambahkan kolom baru
df['Count_Transaction_Group'] = df.apply(func, axis=1)

df_year = df.groupby(['Count_Transaction_Group'])['Customer_ID'].count()
df_year.plot(x='Count_Transaction_Group', 
             y='Customer_ID', 
             kind='bar', 
             title='Customer Distribution by Count Transaction Group')
plt.xlabel('Count Transaction Group')
plt.ylabel('Num of Customer')
plt.tight_layout()
# plt.savefig("kategorisasi.png", format='png')
plt.show()
