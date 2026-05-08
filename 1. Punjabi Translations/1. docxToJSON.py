import os
import re
import json
from docx import Document

# Folder containing .docx files
folder_path = "C:/Files/Punjabi Multifarm dataset/1. Punjabi"

# Output JSON file
output_json = "output.json"

# Store all extracted entries
all_data = []

# Function to read .docx text
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []

    for para in doc.paragraphs:
        full_text.append(para.text)

    return "\n".join(full_text)

# Safe extraction function
def extract(pattern, text):
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""

# Convert to float safely
def to_float(value):
    try:
        return float(value)
    except:
        return None

# Process all .docx files
for filename in os.listdir(folder_path):

    if filename.endswith(".docx"):

        file_path = os.path.join(folder_path, filename)

        # Read text
        text = read_docx(file_path)

        # Split entries using #number
        entries = re.split(r'#\d+', text)

        for entry in entries:

            entry = entry.strip()

            if not entry:
                continue

            # Create structured JSON object
            item = {
                "term_en": extract(r'term_en:\s*(.+)', entry),
                "term_pa": extract(r'term_pa:\s*(.+)', entry),
                "term_roman": extract(r'term_roman:\s*(.+)', entry),
                "base_score": to_float(extract(r'base_score:\s*(.+)', entry)),
                "llm_score": to_float(extract(r'llm_score:\s*(.+)', entry)),
                "final_score": to_float(extract(r'final_score:\s*(.+)', entry)),
                "judge_feedback": {
                    "semantic": to_float(extract(r'semantic:\s*(.+)', entry)),
                    "completeness": to_float(extract(r'completeness:\s*(.+)', entry)),
                    "structure": to_float(extract(r'structure:\s*(.+)', entry)),
                    "final": to_float(extract(r'final:\s*(.+)', entry)),
                    "error": extract(r'error:\s*(.+)', entry)
                }
            }

            all_data.append(item)

# Save JSON file
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f"JSON saved successfully: {output_json}")