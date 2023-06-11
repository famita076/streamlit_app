import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats

# Judul aplikasi
st.title("Uji Hipotesis untuk K Populasi")

# Input data sampel
k = st.number_input("Jumlah Populasi (k)", min_value=2, value=2, step=1)
sample_sizes = []
samples = []

for i in range(k):
    sample_size = st.number_input(f"Ukuran Sampel Populasi {i+1}", min_value=1, value=10, step=1)
    sample_sizes.append(sample_size)

    sample = []
    for j in range(sample_size):
        data = st.number_input(f"Data Sampel {i+1}-{j+1}")
        sample.append(data)
    samples.append(sample)

# Uji hipotesis menggunakan ANOVA
statistic, p_value = stats.f_oneway(*samples)

# Membuat tabel hasil analisis
data = {'Populasi': [], 'Ukuran Sampel': [], 'Rata-rata': [], 'Variansi': []}

for i, sample in enumerate(samples):
    data['Populasi'].append(f'Populasi {i+1}')
    data['Ukuran Sampel'].append(sample_sizes[i])
    data['Rata-rata'].append(np.mean(sample))
    data['Variansi'].append(np.var(sample, ddof=1))

df = pd.DataFrame(data)

# Menampilkan hasil uji hipotesis dan tabel
st.write("Hasil Uji Hipotesis:")
st.write(f"Statistik Uji: {statistic:.4f}")
st.write(f"Nilai p: {p_value:.4f}")

alpha = st.number_input("Tingkat Signifikansi (alpha)", value=0.05)

if p_value < alpha:
    st.write("Kesimpulan: Terdapat perbedaan yang signifikan di antara setidaknya dua populasi.")
else:
    st.write("Kesimpulan: Tidak cukup bukti untuk menyimpulkan adanya perbedaan signifikan di antara populasi.")

st.write("Tabel Analisis:")
st.write(df)
