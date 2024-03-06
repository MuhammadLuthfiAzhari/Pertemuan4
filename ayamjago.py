import pandas as pd

# Membuat contoh dataset
data = {'nama': ['John', 'Jane', 'Bob'],
        'kelas': [2, 1, 3],
        'nilai': [85, 90, 78]}

# Membuat DataFrame dari dataset
df = pd.DataFrame(data)

# Mengganti urutan kolom
df = df[['kelas', 'nama', 'nilai']]

# Menampilkan DataFrame dengan urutan kolom yang baru
print(df)


print("perubahan cuyyy bro")
