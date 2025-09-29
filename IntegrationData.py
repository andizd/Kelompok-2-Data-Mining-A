import pandas as pd

df = pd.read_csv("step1_collected_data.csv")

df.columns = (
    df.columns
    .str.strip()          
    .str.lower()          
    .str.replace("_", " ") 
)

if "year" in df.columns:
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

if "rating" in df.columns:
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").astype(float)

if "title" in df.columns:
    df["title"] = df["title"].astype(str)

if "metascore" in df.columns:
    df["metascore"] = pd.to_numeric(df["metascore"], errors="coerce").fillna(0).astype(int)

output_file = "step2_integrated_data.csv"
df.to_csv(output_file, index=False)

print(f"Data berhasil diintegrasikan dan disimpan ke {output_file}")
print(df.head())