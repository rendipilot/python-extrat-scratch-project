import json

def level_check(block_categories):
    with open(f"output/{block_categories}", "r") as json_file:
        block_categories = json.load(json_file)

    if block_categories["control"] > 5 or block_categories["variables"] > 5:
        level = "Advanced"
    elif block_categories["control"] > 2 or block_categories["operators"] > 2:
        level = "Intermidiate"
    else:
        level = "Beginner"

    print(f"tingkat level pemograman :  {level}")