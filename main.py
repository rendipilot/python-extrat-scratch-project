import zipfile
import json
import os
from datetime import datetime
from blocktype import process_project_data
from level_check import level_check
# from save import save_json_to_mongodb
from dataset import setDataset


def process(file_project):

    # Ambil nama file tanpa ekstensi .sb3
    base_name = os.path.splitext(os.path.basename(file_project))[0]

    # Format tanggal jika ingin menambahkannya di nama output
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file_name = f"{base_name}_data_{date_str}.json"

    output_folder = "output"
    output_file_path = os.path.join(output_folder, output_file_name)

    with zipfile.ZipFile(f"scratch_file/{file_project}", "r") as zip_ref:
        with zip_ref.open('project.json') as json_file:
            project_data = json.load(json_file)

    if "targets" in project_data:
        targets_data = project_data["targets"]

        block_counts = {}
        for target in targets_data:
            sprite_name = target.get("name", "unknown")
            blocks = target.get("blocks", {})

            block_counts[sprite_name] = len(blocks)

        # file count in a sprite as File blockcount
        output_blocks_path = f"output/{base_name}_blockcount_{date_str}.json"
        with open(output_blocks_path, "w") as output_blocks_file:
            json.dump(block_counts, output_blocks_file, indent=2)
            
        # save_json_to_mongodb(input_file_path=output_blocks_path)

        # save data target json as File Data
        with open(output_file_path, "w") as output_file:
            json.dump(targets_data, output_file, indent=2)
            
        # save_json_to_mongodb(input_file_path=output_file_path)
        
        print("berhasil")

        blocktype_output_name = f"{base_name}_blocktype_{date_str}.json"

        # untuk membuat blok type
        # save type count block  as File Blocktype
        process_project_data(input_file_path=output_file_name, output_file_path=blocktype_output_name)
        level_check(block_categories=blocktype_output_name)

        # panggil dataset function
        setDataset(base_name, blocktype_output_name, output_blocks_path)
    else:
        print("gagal")

def main():
    #process()
    scratch_path_folder = "scratch_file"
    for scratch in os.listdir(scratch_path_folder):
        if scratch.endswith(".sb3"):
            print("file = " + scratch)
            process(scratch)

if __name__ == "__main__":
    main()