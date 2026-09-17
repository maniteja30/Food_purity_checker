import pandas as pd
from pathlib import Path

# Anchor to the script's directory, then go UP one level to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
data_file = PROJECT_ROOT / "data" / "raw" / "en.openfoodfacts.org.products.tsv"

df = pd.read_csv(data_file, sep="\t", low_memory=False)
print(df.shape)
print(df.head())
