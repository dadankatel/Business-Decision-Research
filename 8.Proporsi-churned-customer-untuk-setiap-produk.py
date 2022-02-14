"""
Proporsi churned customer untuk setiap produk

Dari sisi churned customer, khususnya untuk melihat seberapa besar proporsi churned customer untuk tiap-tiap produk dapat diketahui insight-nya melalui pie chart.
"""

plt.clf()
# Melakukan pivot data dengan pivot_table
df_piv = df.pivot_table(index='is_churn', # berada di sebelah kiri tabel sebagai parameter
                        columns='Product', # berada di atas sebagai kolom sesuai banyaknya nama product
                        values='Customer_ID',  # nilai yang didalam tabel
                        aggfunc='count', 
                        fill_value=0)
# print(df_piv.head()) # bentuk pivot tabel dapat dilihat dengan fungsi ini
# Mendapatkan Proportion Churn by Product
plot_product = df_piv.count().sort_values(ascending=False).head(5).index # memisahkan setiap product berdasrkan urutan abjad

# Plot pie chartnya
df_piv = df_piv.reindex(columns=plot_product)
df_piv.plot.pie(subplots=True,
                figsize=(10, 7),
                layout=(-1, 2),
                autopct='%1.0f%%',
                title='Proportion Churn by Product', )
plt.tight_layout()
plt.savefig("PieChart", format='png')
plt.show()
