import json
import pandas as pd
from creative import check_creativity_score
from complexity import check_logical_score 
import os

def setDataset(name, blocktype, blockcount):
    with open(f"output/{blocktype}", "r") as json_file:
        block_data = json.load(json_file)


    with open(blockcount, "r") as sprite_file:
        sprite_data = json.load(sprite_file)


    total_blocks = sum(block_data.values())

    print(total_blocks)

    features = {
        "name" : name,
        "total_blocks" : total_blocks,
        "motion_ratio" : block_data["motion"] /total_blocks if total_blocks else 0,
        "looks_ratio" : block_data["looks"] /total_blocks if total_blocks else 0,
        "sound_ratio" : block_data["sound"] /total_blocks if total_blocks else 0,
        "events_ratio" : block_data["events"] /total_blocks if total_blocks else 0,
        "control_ratio" : block_data["control"] /total_blocks if total_blocks else 0,
        "sennsing_ratio": block_data["sensing"] /total_blocks if total_blocks else 0,
        "operators_ratio" : block_data["operators"] /total_blocks if total_blocks else 0,
        "variables_ratio" : block_data["variables"] /total_blocks if total_blocks else 0,
        "myblocks_ratio" : 1 if block_data["myblocks"] > 0 else 0,
    }
    
    creativity_score = check_creativity_score(block_data)
    logical_score = check_logical_score (block_data)
    
    level = 0

    if creativity_score > 75 or logical_score > 75:
        # level = 4
        
        if(creativity_score > logical_score ):
            if(len(blockcount) > 7 and features["total_blocks"] > 40 or features["motion_ratio"] > 0.2 or features["looks_ratio"] >  0.1 or features["sound_ratio"] > 0.1 or features["events_ratio"] > 0.1):
                level = 4
            elif(len(blockcount) > 5 and features["total_blocks"] > 20 or features["motion_ratio"] > 0.2 or features["looks_ratio"] >  0.05 or features["sound_ratio"] > 0.05 or features["events_ratio"] > 0.05):
                level = 3
        else:
            if(features["control_ratio"] > 0.12 and features["total_blocks"] > 40 or features["variables_ratio"] > 0.1 or features["operators_ratio"] > 0.15 or block_data["myblock"] > 1):
                level = 4
            elif(features["control_ratio"] > 0.12 and features["total_blocks"] > 20 or features["variables_ratio"] > 0.05 or features["operators_ratio"] > 0.1):
                level = 3    
    elif  creativity_score > 50 or logical_score > 50:
        # level = 3
        if(creativity_score > logical_score ):
            if(len(blockcount) > 5 and features["total_blocks"] > 30 or features["motion_ratio"] > 0.2 or features["looks_ratio"] >  0.1 or features["sound_ratio"] > 0.1 or features["events_ratio"] > 0.1):
                level = 3
            elif(len(blockcount) > 3 and features["total_blocks"] > 15 or features["motion_ratio"] > 0.2 or features["looks_ratio"] >  0.05 or features["sound_ratio"] > 0.05 or features["events_ratio"] > 0.05):
                level = 2
        else:
            if(features["control_ratio"] > 0.1 and features["total_blocks"] > 30 or features["variables_ratio"] > 0.1 or features["operators_ratio"] > 0.15 or block_data["myblock"] > 1):
                level = 3
            elif(features["control_ratio"] > 0.1 and features["total_blocks"] > 15 or features["variables_ratio"] > 0.05 or features["operators_ratio"] > 0.1):
                level = 2    
    elif creativity_score > 25 or logical_score > 25:
        # level = 2
        if(creativity_score > logical_score ):
            if(len(blockcount) > 3 and features["total_blocks"] > 25 or features["motion_ratio"] > 0.1 or features["looks_ratio"] >  0.1 or features["sound_ratio"] > 0.1 or features["events_ratio"] > 0.1):
                level = 2
            elif(len(blockcount) > 2 and features["total_blocks"] > 12 or features["motion_ratio"] > 0.1 or features["looks_ratio"] >  0.05 or features["sound_ratio"] > 0.05 or features["events_ratio"] > 0.05):
                level = 1
        else:
            if(features["control_ratio"] > 0.1 and features["total_blocks"] > 25 or features["variables_ratio"] > 0.1 or features["operators_ratio"] > 0.15):
                level = 2
            elif(features["control_ratio"] > 0.1 and features["total_blocks"] > 12 or features["variables_ratio"] > 0.05 or features["operators_ratio"] > 0.1):
                level = 1
    elif creativity_score > 10 or logical_score > 10:
        # level = 1
        if(creativity_score > logical_score ):
            if(len(blockcount) > 3 and features["total_blocks"] > 15 or features["motion_ratio"] > 0.1 or features["looks_ratio"] >  0.1 or features["sound_ratio"] > 0.1 or features["events_ratio"] > 0.1):
                level = 1
            elif(len(blockcount) > 2 and features["total_blocks"] > 8 or features["motion_ratio"] > 0.1 or features["looks_ratio"] >  0.05 or features["sound_ratio"] > 0.05 or features["events_ratio"] > 0.05):
                level = 0
        else:
            if(features["control_ratio"] > 0.1 and features["total_blocks"] > 15 or features["variables_ratio"] > 0.1 or features["operators_ratio"] > 0.15):
                level = 2
            elif(features["control_ratio"] > 0.1 and features["total_blocks"] > 8 or features["variables_ratio"] > 0.05 or features["operators_ratio"] > 0.1):
                level = 0
    else:
        level = 0



    features["level"] = level
    features["sprite"] = len(sprite_data)
    features["creativity"] = creativity_score
    features["logical"] = logical_score
    features["complexity"]= creativity_score + logical_score

    df = pd.DataFrame([features])
    file_path = "output/test_dataset.csv"
    mode = "a" if os.path.exists(file_path) else "w"
    df.to_csv(file_path, mode=mode, header=(mode=="w"),index=False)