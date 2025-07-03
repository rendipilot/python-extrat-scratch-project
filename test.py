import zipfile
import json
import os

def save_project_json(sb3_path, output_folder):
    # Pastikan folder tujuan ada, jika tidak, buat foldernya
    os.makedirs(output_folder, exist_ok=True)

    # Buka file .sb3 dan ekstrak project.json
    with zipfile.ZipFile(sb3_path, "r") as zip_ref:
        with zip_ref.open('project.json') as json_file:
            project_data = json.load(json_file)

    # Tentukan path untuk menyimpan file JSON
    base_name = os.path.splitext(os.path.basename(sb3_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}.json")

    # Simpan sebagai file .json
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(project_data, f, ensure_ascii=False, indent=2)

    print(f"project.json berhasil disimpan ke: {output_path}")

# Contoh penggunaan
save_project_json("scratch_file/aisyah-gametabrakanmobil.sb3", "datatest")
