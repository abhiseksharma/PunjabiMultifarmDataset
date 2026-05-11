import json
import pandas as pd

# Input merged JSON file
input_json = "Verified files/merged_json.json"

# Output CSV file
output_csv = "Translations (multifarm).csv"

# Read JSON data
with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract required columns
rows = []

for item in data:

    rows.append([
        item.get("term_en", ""),
        item.get("term_pa", ""),
        item.get("term_roman", "")
    ])

# Create DataFrame with columns 0,1,2
df = pd.DataFrame(rows, columns=["0", "1", "2"])

# Save CSV
df.to_csv(output_csv, index=False, encoding="utf-8-sig")

print(f"CSV saved successfully: {output_csv}")