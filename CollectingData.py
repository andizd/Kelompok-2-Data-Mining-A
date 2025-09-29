import pandas as pd

input_file = "imdb_kaggle.csv"
df = pd.read_csv(input_file)

output_file = "step1_collected_data.csv"
df.to_csv(output_file, index=False)

print(f"Data berhasil dikoleksi dari {input_file} dan disimpan ke {output_file}")
print(df.head())