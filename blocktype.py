import json

def process_project_data(input_file_path, output_file_path):
    # Membaca data proyek dari file JSON
    with open(f"output/{input_file_path}") as json_file:
        project_data = json.load(json_file)

    # Inisialisasi kategori blok
    block_categories = {
        "motion": 0, 
        "looks": 0, 
        "sound": 0, 
        "events": 0, 
        "control": 0, 
        "operators": 0, 
        "variables": 0,
        "sensing": 0, 
        "myblocks": 0
    }

    # Menyusun kategori berdasarkan opcode
    for target in project_data:
        for block_id, block in target.get("blocks", {}).items():
            
            if isinstance(block, list):
                continue 

            opcode = block.get("opcode", "")
            
            
            if "motion" in opcode:
                block_categories["motion"] += 1
            elif "looks" in opcode:
                block_categories["looks"] += 1
            elif "sound" in opcode:
                block_categories["sound"] += 1
            elif "event" in opcode:
                block_categories["events"] += 1
            elif "control" in opcode:
                block_categories["control"] += 1
            elif "sensing" in opcode:
                block_categories["sensing"] += 1
            elif "operator" in opcode:
                block_categories["operators"] += 1
            elif "data" in opcode:
                block_categories["variables"] += 1
            elif "procedures" in opcode:
                block_categories["myblocks"] += 1

    # Menyimpan hasil kategori ke file output
    with open(f"output/{output_file_path}", "w") as output_file:
        json.dump(block_categories, output_file, indent=2)

    print("Berhasil memproses data dan menyimpan ke", output_file_path)
