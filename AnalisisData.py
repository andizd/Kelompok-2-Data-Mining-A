import pandas as pd

df = pd.read_csv("step2_integrated_data.csv")

avg_rating = df["rating"].mean()

film_per_year = df.groupby("year").size().reset_index(name="jumlah_film")

output_file = "step3_analisis_data.csv"
film_per_year.to_csv(output_file, index=False)

print(f"Rata-rata rating: {avg_rating:.2f}")
print(f"Hasil analisis disimpan ke {output_file}")
print(film_per_year.head())