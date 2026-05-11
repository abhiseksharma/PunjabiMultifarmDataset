import os
import json

# Folder containing JSON files
folder_path = "Verified files"

# Output merged JSON file
output_json = folder_path + "/merged_json.json"

# Store merged data
merged_data = []

# Read all JSON files
for filename in os.listdir(folder_path):

    if filename.endswith(".json"):

        file_path = os.path.join(folder_path, filename)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # If file contains a list
                if isinstance(data, list):
                    merged_data.extend(data)

                # If file contains a single object
                elif isinstance(data, dict):
                    merged_data.append(data)

        except Exception as e:
            print(f"Error reading {filename}: {e}")

# Save merged JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(merged_data, f, ensure_ascii=False, indent=4)

print(f"Merged JSON saved successfully: {output_json}")
print(f"Total records merged: {len(merged_data)}")