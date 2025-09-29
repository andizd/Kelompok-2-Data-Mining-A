import pandas as pd

df = pd.read_csv("step3_analisis_data.csv")

missing = df.isnull().sum()

duplicates = df.duplicated().sum()

validation = pd.DataFrame({
    "cek": ["missing_values", "duplicates"],
    "jumlah": [missing.sum(), duplicates]
})

output_file = "step4_validasi_data.csv"
validation.to_csv(output_file, index=False)

print(f"Hasil validasi disimpan ke {output_file}")
print(validation)
