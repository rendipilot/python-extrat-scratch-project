import json

def check_logical_score(project_data):
    complexity_score = 0

    # with open(project_json, "r") as json_file:
    #     project_data = json.load(json_file)

    # for target in project_data:
    #     # print(target)
    #     for block_id, block in target.get("blocks", {}).items():
    #         op = block.get("opcode", "")
    #         # print(op)

    #         if op.startswith("control"):
    #             complexity_score += 2
    #         elif op.startswith("operator"):
    #             complexity_score += 1.5
    #         elif op.startswith("data"):
    #             complexity_score += 1
    #         elif op.startswith("procedures"):
    #             complexity_score += 2
    
    for type in project_data:
        print(f"type = {type} berjumlah = {project_data[type]}")
        if (type == "control"):
            complexity_score += 1 * project_data[type]
        elif (type == "operators"):
            complexity_score += 1 * project_data[type]
        elif (type == "variables"):
            complexity_score += 0.5 * project_data[type]
        elif (type == "sensing"):
            complexity_score += 1 * project_data[type]

    return complexity_score

