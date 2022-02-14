"""
Di bagian ini, selanjutnya akan menentukan feature columns dari dataset yang dimiliki, 
di sini dipilih kolom Average_Transaction_Amount, Count_Transaction, dan Year_Diff. Akan tetapi, kolom terakhir belum ada. 
Silakan dicreate dahulu kolom Year_Diff ini dan kemudian assign dataset dengan feature columns ini sebagai variabel independent X.

Untuk target tentunya persoalan costumer dengan kondisi churn atau tidak, assign dataset untuk target ini ke dalam variabe dependent y.
"""
# Feature column: Year_Diff
df['Year_Diff'] = df['Year_Last_Transaction'] - df['Year_First_Transaction']

# Nama-nama feature columns
feature_columns = ['Average_Transaction_Amount', 'Count_Transaction', 'Year_Diff']

# Features variable menggungkan feature columns
X = df[feature_columns] 

# Target variable / untuk mengetahui kondisi customer akan churn atau tidak
y = df['is_churn'] 
y=y.astype('int')
