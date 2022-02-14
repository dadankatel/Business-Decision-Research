"""
Menghapus kolom yang tidak diperlukan

Pada data sebelumnya terdapat beberapa kolom yang dapat dihapus karena tidak diperlukan yaitu kolom‘no’ dan ‘Row_Num’.
"""
# Hapus kolom-kolom yang tidak diperlukan
del df['no']
del df['Row_Num']

# Cetak lima data teratas
print(df.head())
