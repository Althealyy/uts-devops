import pandas as pd
import os

# ambil data dari environment variable
nilai_str = os.getenv('NILAI', '85,90,78,92,88')

# ubah jadi list integer
nilai = list(map(int, nilai_str.split(',')))

# buat dataframe
df = pd.DataFrame({'Nilai': nilai})

print('--- Analisis Data Menjalankan ---')

# hitung total
total = df['Nilai'].sum()
print(f'Total Nilai: {total}')

print('--- Selesai ---')

# buat folder output
os.makedirs('/app/output', exist_ok=True)

# simpan ke csv
df.to_csv('/app/output/hasil.csv', index=False)

print('Hasil disimpan ke /app/output/hasil.csv')
print('--- Analisis Data Selesai ---')