"""
Average transaction amount by year

Dengan menggunakan seaborn pointplot, visualisasikanlah tren dari tahun ke tahun rata-rata jumlah transaksi untuk tiap-tiap produknya.
"""
import seaborn as sns

plt.clf()
# Pointplot akan menghasilkan grafik titik yang bersambung,
# Data yang dicari yaitu Product dengan berdasrkan tiap tahunnya menggungakan Year_First_Transaction
sns.pointplot(data = df.groupby(['Product', 'Year_First_Transaction']).mean().reset_index(), 
              x='Year_First_Transaction', 
              y='Average_Transaction_Amount', 
              hue='Product'
             )
plt.tight_layout()
plt.show()
